import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Barang(db.Model):
    __tablename__ = 'barang'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    jumlah = db.Column(db.Integer())
    satuan = db.Column(db.String())
    hb = db.Column(db.Float())
    hj = db.Column(db.Float())
    created_at = db.Column(db.DateTime, default =  datetime.datetime.now())
    status_enabled = db.Column(db.Boolean(), default = True)  

    # role_name = db.relationship('Role',cascade="all,delete", backref='Quiz', lazy=True)


    def __init__(self,name,jumlah,satuan,hb,hj):
        self.name = name
        self.jumlah = jumlah
        self.satuan = satuan
        self.hb = hb
        self.hj = hj


    def __repr__(self):
        return '<barang id {}>'.format(self.id)


    def serialise(self):
        # role = Role.query.filter_by(role_id = self.role_id).first()
        # posisi = Posisi.query.filter_by(posisi_id = self.posisi_id).first()
        return {
            'id' : self.id,
            'name' : self.name,
            'jumlah' : self.jumlah,
            'satuan' : self.satuan,
            'hb' : self.hb,
            'hj' : self.hj,
            'created_at' : self.created_at,
            'status_enabled' : self.status_enabled
        }


###############################################

class Transaksi(db.Model):
    __tablename__ = 'transaksi'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    tipe = db.Column(db.String())
    id_barang = db.Column(db.Integer(), db.ForeignKey('barang.id'))
    jumlah = db.Column(db.Integer())
    created_at = db.Column(db.DateTime, default =  datetime.datetime.now())
    status_enabled = db.Column(db.Boolean(), default = True)


    def __init__(self,name,tipe,id_barang,jumlah):
        self.name = name
        self.tipe = tipe
        self.id_barang = id_barang
        self.jumlah = jumlah

    def __repr__(self):
        return '<transaksi id {}>'.format(self.id)

    def serialise(self):
        barang = Barang.query.filter_by(id = self.id_barang).first()

        return {
            'id' : self.id,
            'name' : self.name,
            'tipe' : self.tipe,
            'barang_id' : barang.id,
            'barang_name' : barang.name,
            'barang_harga_beli' : barang.hb,
            'barang_harga_jual' : barang.hj,
            'jumlah' : self.jumlah,                        
            'created_at' : self.created_at,
            'status_enabled' : self.status_enabled
        }
    




###############################################

class CashFlow(db.Model):
    __tablename__ = 'cashflow'

    id = db.Column(db.Integer, primary_key = True)
    created_at = db.Column(db.DateTime, default =  datetime.datetime.now())
    status_enabled = db.Column(db.Boolean(), default = True)

    cash_in = db.Column(db.Float())
    cash_out = db.Column(db.Float())
    balance = db.Column(db.Float())

    id_transaksi = db.Column(db.Integer(), db.ForeignKey('transaksi.id'))
    keterangan = db.Column(db.String())

    def __init__(self,cash_in,cash_out,balance,id_transaksi,keterangan):
        self.cash_in = cash_in
        self.cash_out = cash_out
        self.balance = balance
        self.id_transaksi = id_transaksi
        self.keterangan = keterangan

    def __repr__(self):
        return '<cashflow id {}>'.format(self.id)

    def serialise(self):
        transaksi = Transaksi.query.filter_by(id = self.id_transaksi).first()
        return {
            'id' : self.id,
            'cash_in' : self.cash_in,
            'cash_out' : self.cash_out,
            'balance' : self.balance,
            'transaksi_id' : transaksi.id,
            'transaksi_jumlah' : transaksi.jumlah,
            'keterangan' : self.keterangan,
            'created_at' : self.created_at,
            'status_enabled' : self.status_enabled

        }
        
    