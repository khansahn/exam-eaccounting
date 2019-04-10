
from flask import Flask, request, json, jsonify, make_response
import os, requests

from ..utils.models import *
from ..utils.authorisation import verifyLogin
from . import router

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import exists
from sqlalchemy import func

#####################################################################################################
# ADD BARANG KE TABEL BARANG, TRANSAKSI, DAN CASHFLOW
#####################################################################################################
@router.route('/transaksi/pembelianBarang', methods = ['POST'])
# @verifyLogin

def pembelianBarang():
    body = request.json

    response = {
        "error" : True,
        "message" : "",
        "data" : {}
    }
    errorCode = 404

    # nambah ke tabel barang, transaksi dengan tipe beli, cashflow dengan out
    try:  
        # nambah ke tabel barang
        barang = Barang(
            name = body["nama_barang"],
            satuan = body["satuan"],
            jumlah = body["jumlah"],
            hb = body["harga_beli"],
            hj = body["harga_jual"])
        db.session.add(barang)
        db.session.commit()
        barang.serialise()

        # nambah ke transaksi dengan tipe pembelian
        transaksi = Transaksi(
            name = body["nama_pembelian"],
            tipe = "beli",
            id_barang = barang.id,
            jumlah = barang.jumlah
        )
        db.session.add(transaksi)
        db.session.commit()
        transaksi.serialise
        print(transaksi.serialise())

        # nambah ke table cashflow dengan cash_out        
        cashflow = CashFlow(
            cash_in = 0,
            cash_out = barang.jumlah * barang.hb,
            balance = 0,
            id_transaksi = transaksi.id,
            keterangan = body["nama_pembelian"]
        )        
        db.session.add(cashflow)
        db.session.commit()

        data = {
            "barang" : barang.serialise(),
            "transaksi" : transaksi.serialise(),
            "cashflow" : cashflow.serialise()
        }

        response["message"] =  "Pembelian Barang added to Barang and Transaksi. Barang-id dibeli = {}".format(barang.id)
        response["error"] = False
        response["data"] = data
    except Exception as e:
        response["message"] = str(e)
    finally:
        db.session.close()

    return jsonify(response)



#####################################################################################################
# ADD PENJUALAN BARANG KE TRANSAKSI, DAN CASHFLOW, UPDATE JUMLAH ASET DI BARANG
#####################################################################################################
@router.route('/transaksi/penjualanBarang', methods = ['POST'])
# @verifyLogin

def penjualanBarang():
    body = request.json

    response = {
        "error" : True,
        "message" : "",
        "data" : {}
    }
    errorCode = 404

    # nambah ke tabel transaksi dengan tipe jual, cashflow dengan in
    # update jumlah barang di barang
    try:          
        # cek barang cukup atau ga dl
        barang = db.session.query(Barang).filter_by(id = body["id_barang"]).first()
        barangCukup = False
        if barang.jumlah >= body["jumlah_terjual"]:
            barangCukup = True
        

        if barangCukup == True:


            # nambah ke transaksi dengan tipe penjualan
            transaksi = Transaksi(
                name = body["nama_penjualan"],
                tipe = "jual",
                id_barang = body["id_barang"],
                jumlah = body["jumlah_terjual"]
            )
            db.session.add(transaksi)
            db.session.commit()
            transaksi.serialise
            transaksiA = (transaksi.serialise())

            # nambah ke table cashflow dengan cash_out        
            print(transaksiA["jumlah"] * transaksiA["barang_harga_jual"])  
            cashflow = CashFlow(
                cash_in = transaksiA["jumlah"] * transaksiA["barang_harga_jual"],
                cash_out = 0,
                balance = 0,
                id_transaksi = transaksiA["id"],
                keterangan = body["nama_penjualan"]
            )        
            db.session.add(cashflow)
            db.session.commit()

            # update ke tabel barang
            barang = db.session.query(Barang).filter_by(id = transaksiA["barang_id"]).first()
            barangA = (barang.serialise())
            jumlahSebelumTerjual = barangA["jumlah"]
            jumlahSetelahTerjual = jumlahSebelumTerjual - transaksiA["jumlah"]

            Barang.query.filter_by(id = transaksiA["barang_id"]).update(dict(jumlah=jumlahSetelahTerjual))

            db.session.commit()
            barang.serialise()


            data = {
                "barang" : barang.serialise(),
                "transaksi" : transaksi.serialise(),
                "cashflow" : cashflow.serialise()
            }

            response["message"] =  "Penjualan Barang added to Transaksi. Barang-id terjual = {}".format(barang.id)
            response["error"] = False
            response["data"] = data
        
        else:
            response["message"] = "Barang yang mau dijual lebih dari stock yang ada"
    except Exception as e:
        response["message"] = str(e)
    finally:
        db.session.close()

    return jsonify(response)


#####################################################################################################
# GET CASHFLOW
#####################################################################################################
@router.route('/cashflow/getAll', methods = ['GET'])
# @verifyLogin

def getAllCashFlow():
    # body = request.json

    response = {
        "error" : True,
        "message" : "",
        "data" : {}
    }
    errorCode = 404

    try:          
        cashFlowEnabled = CashFlow.query.filter_by(status_enabled = True).order_by(CashFlow.created_at).all()

        data = ([e.serialise() for e in cashFlowEnabled])

        # UPDATE BALANCE (TP INI GA KEUPDATE DI DB SIH HEU)
        prevBalance = 0
        for d in data:
            d["balance"] = d["cash_in"] - d["cash_out"] + prevBalance
            prevBalance = d["balance"]


        cashFlowEnabledCount  = len(data)
        response["message"] = "CashFlow(s) found : " + str(cashFlowEnabledCount)
        response["error"] = False
        response["data"] = data

    except Exception as e:
        response["message"] = str(e)
    finally:
        db.session.close()

    return jsonify(response)

