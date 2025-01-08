import sys
from PyQt5 import QtWidgets, uic
import psycopg2 as mc
from PyQt5.QtWidgets import QTableWidgetItem
from GUI.Icons import get_icon
from PyQt5.QtWidgets import QMessageBox
from classes.Service1 import Service1

qtcreator_file  = "ui/service1.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowService1(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnCari.clicked.connect(self.search_data)
        self.btnSimpan.clicked.connect(self.save_data)
        self.txtKodeSV.returnPressed.connect(self.search_data)
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")

    def select_data(self):
        try:
            sv = Service1()
            result = sv.getAllData()
            self.gridService1.setHorizontalHeaderLabels(['ID Service', 'Kode Service', 'Jenis Service', 'Harga', 'Merek'])
            self.gridService1.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.gridService1.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.gridService1.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kdsv=self.txtKodeSV.text()           
            sv = Service1()
            result = sv.getByKODESV(kdsv)
            a = sv.affected
            if(a>0):
                self.txtJenisService.setText(result[2])
                self.txtHarga.setText(str(result[3]))
                self.txtMerek.setText(result[4])
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True)
                self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtJenisService.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False)
                self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            sv = Service1()
            kdsv=self.txtKodeSV.text()
            jenis_service=self.txtJenisService.text()
            harga=self.txtHarga.text()
            merek = self.txtMerek.text()
            if(self.edit_mode==False):   
                sv.kode_service = kdsv
                sv.jenis_service = jenis_service
                sv.harga = harga
                sv.merek = merek
                
                a = sv.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Service1 Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Service1 Gagal Tersimpan")
                
                self.clear_entry(self)
                self.select_data()
            elif(self.edit_mode==True):
                sv.kode_service=kdsv
                sv.jenis_service=jenis_service
                sv.harga = harga 
                sv.merek = merek               
                a = sv.updateByKODESERVICE(kdsv)
                if(a>0):
                    self.messagebox("SUKSES", "Data Service1 Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Service1 Gagal Diperbarui")
                self.clear_entry(self)
                self.select_data()
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def delete_data(self, MainWindow):
        try:
            sv = Service1()
            kode_service=self.txtKodeSV.text()
                       
            if(self.edit_mode==True):
                a = sv.deleteByKODESV(kode_service)
                if(a>0):
                    self.messagebox("SUKSES", "Data Service1 Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Service1 Gagal Dihapus")
                
                self.clear_entry(self)
                self.select_data()
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self, MainWindow):
        self.txtKodeSV.setText("")
        self.txtJenisService.setText("")
        self.txtHarga.setText("")
        self.txtMerek.setText("")
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("border: 2px solid goldenrod; border-radius: 10px; padding: 0 8px; background-color: gold; color: rgb(0, 0, 0);")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setStyleSheet("QMessageBox, QPushButton, QLabel {background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.1 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;}")
        mess.setWindowIcon(get_icon("icon"))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

Svr = """ WindowLogin, MainBengkelKendaraan, WindowTransaksi, WindowPelayanan,  WindowPetugas, WindowService1 {
    border-image: url("icons/bengkel1.jpg") 0 0 0 0 stetch stretch; font-color: red; color: white; background-size: auto; background-position: center;
}"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowService1()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowService1()
    app.setStyleSheet(Svr)