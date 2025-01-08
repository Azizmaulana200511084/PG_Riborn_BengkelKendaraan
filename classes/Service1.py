from config.db import DBConnection as mydb
class Service1:
    def __init__(self):
        self.__id_service= None
        self.__kode_service= None
        self.__jenis_service= None
        self.__harga= None
        self.__merek= None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id_service(self):
        return self.__id_service
    
    @property
    def kode_service(self):
        return self.__kode_service

    @kode_service.setter
    def kode_service(self, value):
        self.__kode_service = value
    
    @property
    def jenis_service(self):
        return self.__jenis_service

    @jenis_service.setter
    def jenis_service(self, value):
        self.__jenis_service = value
    
    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, value):
        self.__harga = value

    @property
    def merek(self):
        return self.__merek

    @merek.setter
    def merek(self, value):
        self.__merek = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_service,self.__jenis_service,self.__harga,self.__merek)
        sql="INSERT INTO service1 (kode_service,jenis_service,harga,merek) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id_service):
        self.conn = mydb()
        val = (self.__kode_service,self.__jenis_service,self.__harga,self.__merek, id_service)
        sql="UPDATE service1 SET kode_service=%s, jenis_service=%s, harga=%s, merek=%s WHERE id_service=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateByKODESERVICE(self, kode_service):
        self.conn = mydb()
        val = (self.__kode_service,self.__jenis_service,self.__harga,self.__merek, kode_service)
        sql="UPDATE service1 SET kode_service=%s, jenis_service=%s, harga=%s, merek=%s WHERE kode_service=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id_service):
        self.conn = mydb()
        sql="DELETE FROM service1 WHERE id_service='" + str(id_service) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteByKODESV(self, kode_service):
        self.conn = mydb()
        sql="DELETE FROM service1 WHERE kode_service='" + str(kode_service) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id_service):
        a=str(id_service)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM service1 WHERE id_service='" + b + "'"
        self.result = self.conn.findOne(sql)
        self.__id_service = str(self.result[0])
        self.__kode_service = self.result[1]                   
        self.__jenis_service = self.result[2]                   
        self.__harga = self.result[3] 
        self.__merek = self.result[4]                  
        self.conn.disconnect
        return self.result
        
    def getByKODESV(self, kode_service):
        a=str(kode_service)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM service1 WHERE kode_service='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_service = self.result[1]
            self.__jenis_service = self.result[2]
            self.__harga = str(self.result[3])
            self.__merek = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_service = ''                  
            self.__jenis_service = ''                  
            self.__harga = '' 
            self.__merek = ''                 
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM service1"
        self.result = self.conn.findAll(sql)
        return self.result
