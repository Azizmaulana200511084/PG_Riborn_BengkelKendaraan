import sys
from PyQt5 import QtWidgets, uic
import psycopg2 as mc
from PyQt5.QtWidgets import QTableWidgetItem
from GUI.Icons import get_icon
from PyQt5.QtWidgets import QMessageBox
from classes.Pelayanan import Pelayanan
from classes.Service1 import Service1

qtcreator_file  = "ui/pelayanan.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class WindowPelayanan(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnCari.clicked.connect(self.search_data)
        self.btnSimpan.clicked.connect(self.save_data)
        self.txtKodePelayanan.returnPressed.connect(self.search_data)
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.btnCariIdService.clicked.connect(self.cari_idservice)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;")

    def cari_idservice(self):
        try:           
            id_service=self.txtIDSERVICE.text()           
            sv =Service1()
            result = sv.getByID(id_service)           
            a = sv.affected
            
            if(a!=0):
                self.txtJenisService.setText(sv.jenis_service.strip())
            else:
                self.messagebox("INFO", "Data Service tidak ditemukan")
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def select_data(self):
        try:
            pln = Pelayanan()
            result = pln.getAllData()

            self.gridPelayanan.setHorizontalHeaderLabels(['ID Pelayanan', 'Kode Pelayanan', 'Jasa Pelayanan', 'Jenis Kendaraan', 'id_service'])
            self.gridPelayanan.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                self.gridPelayanan.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.gridPelayanan.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kode_pelayanan=self.txtKodePelayanan.text()           
            pln = Pelayanan()
            result = pln.getByKodePLN(kode_pelayanan)
            a = pln.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.JenisKendaraan.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False)
                self.btnHapus.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            pln = Pelayanan()
            kode_pelayanan=self.txtKodePelayanan.text()
            if self.ServiceRingan.isChecked():
                jasa_pelayanan="Service Ringan"
            
            if self.ServiceBesar.isChecked():
                jasa_pelayanan="Service Besar"
            jenis_kendaraan=self.JenisKendaraan.currentText()
            id_service = self.txtIDSERVICE.text()
            
            if(self.edit_mode==False):   
                pln.kode_pelayanan = kode_pelayanan
                pln.jasa_pelayanan = jasa_pelayanan
                pln.jenis_kendaraan = jenis_kendaraan
                pln.id_service = id_service
                a = pln.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Pelayanan Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Pelayanan Gagal Tersimpan")
                
                self.clear_entry(self)
                self.select_data()
            elif(self.edit_mode==True):
                pln.jasa_pelayanan = jasa_pelayanan
                pln.jenis_kendaraan = jenis_kendaraan
                pln.id_service = id_service
                a = pln.updateByKodePLN(kode_pelayanan)
                if(a>0):
                    self.messagebox("SUKSES", "Data Pelayanan Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Pelayanan Gagal Diperbarui")
                
                self.clear_entry(self)
                self.select_data()
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def delete_data(self, MainWindow):
        try:
            pln = Pelayanan()
            kode_pelayanan=self.txtKodePelayanan.text()
                       
            if(self.edit_mode==True):
                a = pln.deleteByKodePLN(kode_pelayanan)
                if(a>0):
                    self.messagebox("SUKSES", "Data Pelayanan Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Pelayanan Gagal Dihapus")
                
                self.clear_entry(self)
                self.select_data()
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        pln = Pelayanan()
        self.txtKodePelayanan.setText(result[1])
        if(result[2]=="Service Ringan"):
            self.ServiceRingan.setChecked(True)
            self.ServiceBesar.setChecked(False)
        else:
            self.ServiceRingan.setChecked(False)
            self.ServiceBesar.setChecked(True)

        self.JenisKendaraan.setCurrentText(result[3])
        self.txtIDSERVICE.setText(str(result[4]))
        self.cari_idservice()
        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.btnHapus.setEnabled(True)
        self.btnHapus.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;")

    def clear_entry(self, MainWindow):
        self.txtKodePelayanan.setText("")
        self.ServiceRingan.setChecked(False)
        self.ServiceBesar.setChecked(False)
        self.JenisKendaraan.setCurrentText("")
        self.txtIDSERVICE.setText("")
        self.txtJenisService.setText("")
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setStyleSheet("QMessageBox, QPushButton, QLabel {background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.1 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;}")
        mess.setWindowIcon(get_icon("icon"))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

Pyn = """ WindowLogin, MainBengkelKendaraan, WindowTransaksi, WindowPelayanan,  WindowPetugas, WindowService1 {
    border-image: url("icons/bengkel1.jpg") 0 0 0 0 stetch stretch; font-color: red; color: white; background-size: auto; background-position: center;
}"""


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowPelayanan()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowPelayanan()
    app.setStyleSheet(Pyn)