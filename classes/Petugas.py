from config.db import DBConnection as mydb
import hashlib
class Petugas:
    def __init__(self):
        self.__id_petugas=None
        self.__nama_petugas=None
        self.__pssword1=None
        self.__no_telp=None
        self.__email_petugas=None
        self.__rolename= None
        self.__info = None
        self.__loginvalid = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def info(self):
        if(self.__info==None):
            return "NAMA PETUGAS:" + self.__nama_petugas + "\n" + "KATA SANDI:" + self.__pssword1 + "\n" + "NO TELEPON:" + self.__no_telp + "\n" + "EMAIL:" + self.__email_petugas + "\n" + "ROLENAME:" + self.__rolename
        else:
            return self.__info
    
    @info.setter
    def info(self, value):
        self.__info = value

    @property
    def id_petugas(self):
        return self.__id_petugas

    @property
    def nama_petugas(self):
        return self.__nama_petugas

    @nama_petugas.setter
    def nama_petugas(self, value):
        self.__nama_petugas = value

    @property
    def pssword1(self):
        return self.__pssword1

    @pssword1.setter
    def pssword1(self, value):
        self.__pssword1 = value

    @property
    def no_telp(self):
        return self.__no_telp

    @no_telp.setter
    def no_telp(self, value):
        self.__no_telp = value

    @property
    def email_petugas(self):
        return self.__email_petugas

    @email_petugas.setter
    def email_petugas(self, value):
        self.__email_petugas = value

    @property
    def rolename(self):
        return self.__rolename

    @rolename.setter
    def rolename(self, value):
        self.__rolename = value

    @property
    def loginvalid(self):
        return self.__loginvalid

    @loginvalid.setter
    def loginvalid(self, value):
        self.__loginvalid = value
   
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama_petugas, self.__pssword1, self.__no_telp, self.__email_petugas, self.__rolename)
        sql="INSERT INTO petugas (nama_petugas, pssword1, no_telp, email_petugas, rolename) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id_petugas):
        self.conn = mydb()
        val = (self.__nama_petugas, self.__pssword1, self.__no_telp, self.__email_petugas, self.__rolename, id_petugas)
        sql="UPDATE petugas SET nama_petugas = %s, pssword1 = %s, no_telp=%s, email_petugas=%s, rolename=%s WHERE id_petugas=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNamaPetugas(self, nama_petugas):
        self.conn = mydb()
        val = (self.__pssword1, self.__no_telp, self.__email_petugas, self.__rolename, nama_petugas)
        sql="UPDATE petugas SET pssword1 = %s, no_telp=%s, email_petugas=%s, rolename=%s WHERE nama_petugas=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id_petugas):
        self.conn = mydb()
        sql="DELETE FROM petugas WHERE id_petugas='" + str(id_petugas) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNamaPetugas(self, nama_petugas):
        self.conn = mydb()
        sql="DELETE FROM petugas WHERE nama_petugas='" + str(nama_petugas) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByIDNamaPetugas(self, id_petugas):
        a=str(id_petugas)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM petugas WHERE id_petugas='" + b + "'"
        self.result = self.conn.findOne(sql)
        self.__id_petugas = str(self.result[0])
        self.__nama_petugas = self.result[1]
        self.__pssword1 = self.result[2]
        self.__no_telp = self.result[3]
        self.__email_petugas = self.result[4]
        self.__rolename = self.result[5]
        self.conn.disconnect
        return self.result

    def getByPetugas(self, nama_petugas):
        a=str(nama_petugas)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM petugas WHERE nama_petugas='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id_petugas = str(self.result[0])
            self.__nama_petugas = self.result[1]
            self.__pssword1 = self.result[2]
            self.__no_telp = self.result[3]
            self.__email_petugas = self.result[4]
            self.__rolename = self.result[5]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nama_petugas = ''
            self.__pssword1 = ''
            self.__no_telp = ''
            self.__email_petugas = ''
            self.__rolename = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM petugas"
        self.result = self.conn.findAll(sql)
        return self.result

    def Validasi(self, nama_petugas, pssword1):
        a=str(nama_petugas)
        b=a.strip()
        pwd=str(pssword1).strip().encode()
        c = hashlib.md5(pwd)
        c2=c.hexdigest()
        self.conn = mydb()
        sql="SELECT * FROM petugas WHERE nama_petugas='" + b + "' and pssword1='" + c2 + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nama_petugas = self.result[1]
            self.__pssword1 = self.result[2]
            self.__no_telp = self.result[3]
            self.__email_petugas = self.result[4]
            self.__rolename = self.result[5]
            self.affected = self.conn.cursor.rowcount
            val = [True,self.__rolename]
            self.__loginvalid = True
        else:
            self.__nama_petugas = ''                  
            self.__pssword1 = ''
            self.__no_telp = ''
            self.__email_petugas = ''               
            self.__rolename = ''                  
            self.affected = 0
            val = [False,""]
            self.__loginvalid = False
        self.conn.disconnect
        return val


"""ptg = Petugas()
a = mydb()
sql="SELECT * FROM petugas"
cur = a.findAll(sql)
# Get all 
result = ptg.getAllData()
print(result)"""