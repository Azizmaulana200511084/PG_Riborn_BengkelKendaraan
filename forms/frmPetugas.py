import sys
import hashlib
import psycopg2 as mc
from GUI.Icons import get_icon
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Petugas import Petugas

qtcreator_file  = "ui/petugas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowPetugas(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnCari.clicked.connect(self.search_data)
        self.btnSimpan.clicked.connect(self.save_data)
        self.txtNamaUsers.returnPressed.connect(self.search_data)
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.btnKodeUnik.clicked.connect(self.kode_unik)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;")

    def kode_unik(self):
        pwd = self.txtPsw.text()
        h = hashlib.md5(pwd.encode("utf-8")).hexdigest()
        self.txtPsw.setText(str(h))

    def select_data(self):
        try:
            ptg = Petugas()
            result = ptg.getAllData()

            self.gridPetugas.setHorizontalHeaderLabels(['ID Petugas', 'Nama Petugas', 'Kata Sandi', 'Telepon', 'Email', 'Rolename'])
            self.gridPetugas.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                self.gridPetugas.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.gridPetugas.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            nama_petugas=self.txtNamaUsers.text()           
            ptg = Petugas()
            result = ptg.getByPetugas(nama_petugas)
            a = ptg.affected
            if(a>0):
                self.txtPsw.setText(result[2])
                self.txtNoTelp.setText(result[3])
                self.txtEmailPtg.setText(result[4])
                self.txtRolename.setText(result[5])
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True)
                self.btnHapus.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtPsw.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False)
                self.btnHapus.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            ptg = Petugas()
            nama_petugas=self.txtNamaUsers.text()
            pssword1=self.txtPsw.text()
            no_telp =self.txtNoTelp.text()
            email_petugas = self.txtEmailPtg.text()
            self.kode_unik()
            rolename=self.txtRolename.text()
            
            if(self.edit_mode==False):   
                ptg.nama_petugas = nama_petugas
                ptg.pssword1 = pssword1
                ptg.no_telp = no_telp
                ptg.email_petugas = email_petugas
                ptg.rolename = rolename
                a = ptg.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Petugas Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Petugas Gagal Tersimpan")
                
                self.clear_entry(self)
                self.select_data()
            elif(self.edit_mode==True):
                ptg.nama_petugas = nama_petugas
                ptg.pssword1 = pssword1
                ptg.no_telp = no_telp
                ptg.email_petugas = email_petugas
                ptg.rolename = rolename
                a = ptg.updateByNamaPetugas(nama_petugas)
                if(a>0):
                    self.messagebox("SUKSES", "Data Petugas Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Petugas Gagal Diperbarui")
                
                self.clear_entry(self)
                self.select_data()
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self, MainWindow):
        try:
            ptg = Petugas()
            nama_petugas=self.txtNamaUsers.text()
                       
            if(self.edit_mode==True):
                a = ptg.deleteByNamaPetugas(nama_petugas)
                if(a>0):
                    self.messagebox("SUKSES", "Data Petugas Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Petugas Gagal Dihapus")
                
                self.clear_entry(self)
                self.select_data()
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self, MainWindow):
        self.txtNamaUsers.setText("")
        self.txtPsw.setText("")
        self.txtNoTelp.setText("")
        self.txtEmailPtg.setText("")
        self.txtRolename.setText("")
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setStyleSheet("QMessageBox, QPushButton, QLabel {background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.1 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;}")
        mess.setWindowIcon(get_icon("icon"))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

Pts = """ WindowLogin, MainBengkelKendaraan, WindowTransaksi, WindowPelayanan,  WindowPetugas, WindowService1 {
    border-image: url("icons/bengkel1.jpg") 0 0 0 0 stetch stretch; font-color: red; color: white; background-size: auto; background-position: center;
}"""


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowPetugas()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowPetugas()
    app.setStyleSheet(Pts)