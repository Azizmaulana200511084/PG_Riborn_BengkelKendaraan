from config.db import DBConnection as mydb

class Transaksi:
    def __init__(self):
        self.__id_transaksi=None
        self.__nomor_transaksi=None
        self.__nama_pelanggan=None
        self.__nomor_polisi=None
        self.__kode_pelayanan=None
        self.__waktu_pelayanan=None
        self.__waktu_selesai=None
        self.__tanggal_transaksi=None
        self.__kode_service1=None
        self.__kode_service2=None
        self.__kode_service3=None
        self.__total_biaya=None
        self.__uang_masuk=None
        self.__uang_kembali=None
        self.__id_petugas=None
        self.__status_transaksi=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def info(self):
        if(self.__info==None):
            return "Nomor Transaksi:" + self.__nomor_transaksi + "\n" + "Nama Pelanggan:" + self.__nama_pelanggan + "\n" + "Nomor Polisi:" + self.__nomor_polisi + "\n" + "Kode Pelayanan:" + self.__kode_pelayanan + "\n" + "Waktu Pelayanan:" + self.__waktu_pelayanan + "\n" + "Waktu Selesai:" + self.__waktu_selesai + "\n" + "Tanggal Transaksi:" + self.__tanggal_transaksi + "\n" + "Kode Service1:" + self.__kode_service1 + "\n" + "Kode Service2:" + self.__kode_service2 + "\n" + "Kode Service3:" + self.__kode_service3 + "\n" + "Total Biaya:" + self.__total_biaya + "\n" + "Uang Masuk:" + self.__uang_masuk + "\n" + "Uang Kembali:" + self.__uang_kembali + "\n" + "ID Petugas:" + self.__id_petugas + "\n" + "Status Transaksi:" + self.__status_transaksi
        else:
            return self.__info

    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id_transaksi(self):
        return self.__id_transaksi

    @property
    def nomor_transaksi(self):
        return self.__nomor_transaksi

    @nomor_transaksi.setter
    def nomor_transaksi(self, value):
        self.__nomor_transaksi = value

    @property
    def nama_pelanggan(self):
        return self.__nama_pelanggan

    @nama_pelanggan.setter
    def nama_pelanggan(self, value):
        self.__nama_pelanggan = value

    @property
    def nomor_polisi(self):
        return self.__nomor_polisi

    @nomor_polisi.setter
    def nomor_polisi(self, value):
        self.__nomor_polisi = value

    @property
    def kode_pelayanan(self):
        return self.__kode_pelayanan

    @kode_pelayanan.setter
    def kode_pelayanan(self, value):
        self.__kode_pelayanan = value

    @property
    def waktu_pelayanan(self):
        return self.__waktu_pelayanan

    @waktu_pelayanan.setter
    def waktu_pelayanan(self, value):
        self.__waktu_pelayanan = value

    @property
    def waktu_selesai(self):
        return self.__waktu_selesai

    @waktu_selesai.setter
    def waktu_selesai(self, value):
        self.__waktu_selesai = value

    @property
    def tanggal_transaksi(self):
        return self.__tanggal_transaksi

    @tanggal_transaksi.setter
    def tanggal_transaksi(self, value):
        self.__tanggal_transaksi = value

    @property
    def kode_service1(self):
        return self.__kode_service1

    @kode_service1.setter
    def kode_service1(self, value):
        self.__kode_service1 = value

    @property
    def kode_service2(self):
        return self.__kode_service2

    @kode_service2.setter
    def kode_service2(self, value):
        self.__kode_service2 = value

    @property
    def kode_service3(self):
        return self.__kode_service3

    @kode_service3.setter
    def kode_service3(self, value):
        self.__kode_service3 = value

    @property
    def total_biaya(self):
        return self.__total_biaya

    @total_biaya.setter
    def total_biaya(self, value):
        self.__total_biaya = value

    @property
    def uang_masuk(self):
        return self.__uang_masuk

    @uang_masuk.setter
    def uang_masuk(self, value):
        self.__uang_masuk = value

    @property
    def uang_kembali(self):
        return self.__uang_kembali

    @uang_kembali.setter
    def uang_kembali(self, value):
        self.__uang_kembali = value

    @property
    def id_petugas(self):
        return self.__id_petugas

    @id_petugas.setter
    def id_petugas(self, value):
        self.__id_petugas = value

    @property
    def status_transaksi(self):
        return self.__status_transaksi

    @status_transaksi.setter
    def status_transaksi(self, value):
        self.__status_transaksi = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nomor_transaksi, self.__nama_pelanggan, self.__nomor_polisi, self.__kode_pelayanan, self.__waktu_pelayanan, self.__waktu_selesai, self.__tanggal_transaksi, self.__kode_service1, self.__kode_service2, self.__kode_service3, self.__total_biaya, self.__uang_masuk, self.__uang_kembali, self.__id_petugas, self.__status_transaksi)
        sql="INSERT INTO transaksi (nomor_transaksi, nama_pelanggan, nomor_polisi, kode_pelayanan, waktu_pelayanan, waktu_selesai, tanggal_transaksi, kode_service1, kode_service2, kode_service3, total_biaya, uang_masuk, uang_kembali, id_petugas, status_transaksi) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id_transaksi):
        self.conn = mydb()
        val = (self.__nomor_transaksi, self.__nama_pelanggan, self.__nomor_polisi,self.__kode_pelayanan, self.__waktu_pelayanan, self.__waktu_selesai, self.__tanggal_transaksi, self.__kode_service1, self.__kode_service2, self.__kode_service3, self.__total_biaya, self.__uang_masuk, self.__uang_kembali, self.__id_petugas, self.__status_transaksi , id_transaksi)
        sql="UPDATE transaksi SET nomor_transaksi = %s, nama_pelanggan=%s, nomor_polisi=%s, kode_pelayanan=%s, waktu_pelayanan=%s, waktu_selesai=%s, tanggal_transaksi=%s, kode_service1=%s, kode_service2=%s, kode_service3=%s, total_biaya=%s, uang_masuk=%s, uang_kembali=%s, id_petugas=%s, status_transaksi=%s WHERE id_transaksi=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKodeTrs(self, nomor_transaksi):
        self.conn = mydb()
        val = (self.__nama_pelanggan, self.__nomor_polisi, self.__kode_pelayanan, self.__waktu_pelayanan, self.__waktu_selesai, self.__tanggal_transaksi, self.__kode_service1, self.__kode_service2, self.__kode_service3, self.__total_biaya, self.__uang_masuk, self.__uang_kembali, self.__id_petugas, self.__status_transaksi, nomor_transaksi)
        sql="UPDATE transaksi SET nama_pelanggan=%s, nomor_polisi=%s, kode_pelayanan=%s, waktu_pelayanan=%s, waktu_selesai=%s, tanggal_transaksi=%s, kode_service1=%s, kode_service2=%s, kode_service3=%s, total_biaya=%s, uang_masuk=%s, uang_kembali=%s, id_petugas=%s, status_transaksi=%s WHERE nomor_transaksi=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id_transaksi):
        self.conn = mydb()
        sql="DELETE FROM transaksi WHERE id_transaksi='" + str(id_transaksi) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKodeTrs(self, nomor_transaksi):
        self.conn = mydb()
        sql="DELETE FROM transaksi WHERE nomor_transaksi='" + str(nomor_transaksi) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id_transaksi):
        self.conn = mydb()
        sql="SELECT * FROM transaksi WHERE id_transaksi='" + str(id_transaksi) + "'"
        self.result = self.conn.findOne(sql)
        self.__nomor_transaksi = self.result[1]
        self.__nama_pelanggan = self.result[2]
        self.__nomor_polisi = self.result[3]
        self.__kode_pelayanan = str(self.result[4])
        self.__waktu_pelayanan = self.result[5]
        self.__waktu_selesai = self.result[6]
        self.__tanggal_transaksi = self.result[7]
        self.__kode_service1 = self.result[8]
        self.__kode_service2 = self.result[9]
        self.__kode_service3 = self.result[10]
        self.__total_biaya = self.result[11]
        self.__uang_masuk = self.result[12]
        self.__uang_kembali = self.result[13]
        self.__id_petugas = self.result[14]
        self.__status_transaksi = self.result[15]
        self.conn.disconnect
        return self.result

    def getByKodeTrs(self, nomor_transaksi):
        a=str(nomor_transaksi)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM transaksi WHERE nomor_transaksi='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nomor_transaksi = str(self.result[1])
            self.__nama_pelanggan = self.result[2]
            self.__nomor_polisi = self.result[3]
            self.__kode_pelayanan = self.result[4]
            self.__waktu_pelayanan = str(self.result[5])
            self.__waktu_selesai = str(self.result[6])
            self.__tanggal_transaksi = self.result[7]
            self.__kode_service1 = self.result[8]
            self.__kode_service2 = self.result[9]
            self.__kode_service3 = self.result[10]
            self.__total_biaya = str(self.result[11])
            self.__uang_masuk = str(self.result[12])
            self.__uang_kembali = str(self.result[13])
            self.__id_petugas = str(self.result[14])
            self.__status_transaksi = self.result[15]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nomor_transaksi = ''
            self.__nama_pelanggan = ''
            self.__nomor_polisi = ''
            self.__kode_pelayanan = ''
            self.__waktu_pelayanan = ''
            self.__waktu_selesai = ''
            self.__tanggal_transaksi = ''
            self.__kode_service1 = ''
            self.__kode_service2 = ''
            self.__kode_service3 = ''
            self.__total_biaya = ''
            self.__uang_masuk = ''
            self.__uang_kembali = ''
            self.__id_petugas = ''
            self.__status_transaksi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM transaksi"
        self.result = self.conn.findAll(sql)
        return self.result
