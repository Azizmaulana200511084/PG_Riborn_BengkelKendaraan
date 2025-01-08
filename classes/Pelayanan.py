from config.db import DBConnection as mydb

class Pelayanan:

    def __init__(self):
        self.__id_pelayanan=None
        self.__kode_pelayanan=None
        self.__jasa_pelayanan=None
        self.__jenis_kendaraan=None
        self.__id_service=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
        
        
    @property
    def info(self):
        if(self.__info==None):
            return "Kode Pelayanan:" + self.__kode_pelayanan + "\n" + "Jenis Pelayanan" + self.__jasa_pelayanan + "\n" + "Jenis Kendaraan:" + self.__jenis_kendaraan + "\n" + "ID Service" + self.__id_service
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id_pelayanan(self):
        return self.__id_pelayanan

    @property
    def kode_pelayanan(self):
        return self.__kode_pelayanan

    @kode_pelayanan.setter
    def kode_pelayanan(self, value):
        self.__kode_pelayanan = value

    @property
    def jasa_pelayanan(self):
        return self.__jasa_pelayanan

    @jasa_pelayanan.setter
    def jasa_pelayanan(self, value):
        self.__jasa_pelayanan = value

    @property
    def jenis_kendaraan(self):
        return self.__jenis_kendaraan

    @jenis_kendaraan.setter
    def jenis_kendaraan(self, value):
        self.__jenis_kendaraan = value

    @property
    def id_service(self):
        return self.__id_service

    @id_service.setter
    def id_service(self, value):
        self.__id_service = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_pelayanan, self.__jasa_pelayanan, self.__jenis_kendaraan, self.__id_service)
        sql="INSERT INTO pelayanan (kode_pelayanan, jasa_pelayanan, jenis_kendaraan, id_service) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id_pelayanan):
        self.conn = mydb()
        val = (self.__kode_pelayanan, self.__jasa_pelayanan, self.__jenis_kendaraan,self.__id_service , id_pelayanan)
        sql="UPDATE pelayanan SET kode_pelayanan = %s, jasa_pelayanan=%s, jenis_kendaraan=%s, id_service=%s WHERE id_pelayanan=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKodePLN(self, kode_pelayanan):
        self.conn = mydb()
        val = (self.__jasa_pelayanan, self.__jenis_kendaraan, self.__id_service, kode_pelayanan)
        sql="UPDATE pelayanan SET jasa_pelayanan=%s, jenis_kendaraan=%s, id_service=%s WHERE kode_pelayanan=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id_pelayanan):
        self.conn = mydb()
        sql="DELETE FROM pelayanan WHERE id_pelayanan='" + str(id_pelayanan) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKodePLN(self, kode_pelayanan):
        self.conn = mydb()
        sql="DELETE FROM pelayanan WHERE kode_pelayanan='" + str(kode_pelayanan) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id_pelayanan):
        self.conn = mydb()
        sql="SELECT * FROM pelayanan WHERE id_pelayanan='" + str(id_pelayanan) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_pelayanan = self.result[1]
        self.__jasa_pelayanan = self.result[2]
        self.__jenis_kendaraan = self.result[3]
        self.__id_service = str(self.result[4])
        self.conn.disconnect
        return self.result

    def getByKodePLN(self, kode_pelayanan):
        a=str(kode_pelayanan)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM pelayanan WHERE kode_pelayanan='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_pelayanan = self.result[1]
            self.__jasa_pelayanan = self.result[2]
            self.__jenis_kendaraan = self.result[3]
            self.__id_service = str(self.result[4])
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_pelayanan = ''
            self.__jasa_pelayanan = ''
            self.__jenis_kendaraan = ''
            self.__id_service = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM pelayanan"
        self.result = self.conn.findAll(sql)
        return self.result
