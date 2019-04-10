
from flask import Flask, request, json, jsonify, make_response
import os

from ..utils.models import *
from ..utils.authorisation import verifyLogin


from . import router

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import exists
from sqlalchemy import func


#################################################################################################
# GET BARANG
#################################################################################################
@router.route('/master/barang/getAll', methods=['GET'])
# @verifyLogin

def getAllBarang():
    response = {
        "error" : True,
        "message" : "",
        "data" : {}
    }
    
    try:
        barangEnabled = Barang.query.filter_by(status_enabled = True).order_by(Barang.id).all()

        data = [e.serialise() for e in barangEnabled]
        barangEnabledCount  = len(data)
        response["message"] = "Barang(s) found : " + str(barangEnabledCount)
        response["error"] = False
        response["data"] = data
    except Exception as e:
        response["message"] = str(e)
    finally:
        db.session.close()

    
    return jsonify(response)
