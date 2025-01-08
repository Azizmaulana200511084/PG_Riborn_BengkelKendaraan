import sys
from PyQt5 import QtWidgets, uic
from GUI.Icons import get_icon
import psycopg2 as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Transaksi import Transaksi
from classes.Service1 import Service1
from classes.Petugas import Petugas
from classes.Pelayanan import Pelayanan
qtcreator_file  = "ui/transaksi.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)
class WindowTransaksi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnCari.clicked.connect(self.search_data)
        self.btnSimpan.clicked.connect(self.save_data)
        self.txtKodePelayanan.returnPressed.connect(self.search_data)
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.btnCariKodePelayanan.clicked.connect(self.cari_pelayanan)
        self.btnCariIDPetugas.clicked.connect(self.cari_petugas)
        self.btnCariKodeService1.clicked.connect(self.cari_service1)
        self.btnCariKodeService2.clicked.connect(self.cari_service2)
        self.btnCariKodeService3.clicked.connect(self.cari_service3)
        self.btnCariJumblah.clicked.connect(self.cari_jumblah)
        self.btnCariKembalian.clicked.connect(self.cari_hitungDuit)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;")

    def cari_pelayanan(self):
        try:           
            tss=self.txtKodePelayanan.text()           
            pln =Pelayanan()
            result = pln.getByKodePLN(tss)           
            a = pln.affected
            if(a!=0):
                self.txtJasaPelayanan.setText(pln.jasa_pelayanan.strip())
            else:
                self.messagebox("INFO", "Data Pelayanan tidak ditemukan")
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_petugas(self):
        try:           
            tss=self.txtIDPetugas.text()           
            ptg =Petugas()
            result = ptg.getByIDNamaPetugas(tss)           
            a = ptg.affected
            if(a!=0):
                self.txtNamaPetugas.setText(ptg.nama_petugas.strip())
            else:
                self.messagebox("INFO", "Data Petugas tidak ditemukan")
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_service1(self):
        try:
            svr = Service1()
            tss = self.txtKodeService1.text()
            svr.getByKODESV(tss)
            a = svr.affected
            if(a!=0):
                self.txtJenisService1.setText(svr.jenis_service.strip())
                self.txtHarga1.setText(svr.harga.strip())                                              
            else:
                self.messagebox("INFO", "Data Service1 tidak ditemukan")
        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_service2(self):
        try:
            svr = Service1()
            tss = self.txtKodeService2.text()
            svr.getByKODESV(tss)
            a = svr.affected
            if(a!=0):
                self.txtJenisService2.setText(svr.jenis_service.strip())
                self.txtHarga2.setText(svr.harga.strip())                                              
            else:
                self.messagebox("INFO", "Data Service2 tidak ditemukan")
        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_service3(self):
        try:
            svr = Service1()
            tss = self.txtKodeService3.text()
            svr.getByKODESV(tss)
            a = svr.affected
            if(a!=0):
                self.txtJenisService3.setText(svr.jenis_service.strip())
                self.txtHarga3.setText(svr.harga.strip())                                              
            else:
                self.messagebox("INFO", "Data Service3 tidak ditemukan")
        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_jumblah(self):
        if len(self.txtHarga1.text())!=0:
            a=int(self.txtHarga1.text())
        else:
            a=0
        if len(self.txtHarga2.text())!=0:
            b=int(self.txtHarga2.text())
        else:
            b=0
        if len(self.txtHarga3.text())!=0:
            c=int(self.txtHarga3.text())
        else:
            c=0
        jumblah = a+b+c
        self.txtTotalBiaya.setText(str(jumblah))

    def cari_hitungDuit(self):
        if len(self.txtUangMasuk.text())!=0:
            a=int(self.txtUangMasuk.text())
        else:
            a=0
        if len(self.txtTotalBiaya.text())!=0:
            b=int(self.txtTotalBiaya.text())
        else:
            b=0
        jumblah = a-b
        self.txtUangKembali.setText(str(jumblah))

    def select_data(self):
        try:
            tss = Transaksi()
            result = tss.getAllData()
            self.gridTransaksi.setHorizontalHeaderLabels(['ID Transaksi', 'Nomor Transaksi', 'Nama Pelanggan', 'Nomor Polisi', 'Kode Pelayanan', 'Waktu Pelayanan', 'Waktu Selesai', 'Tanggal Transaksi', 'Kode Service1', 'Kode Service2', 'Kode Service3', 'Total Biaya', 'Uang Masuk', 'Uang Kembali', 'ID Petugas', 'Status Transaksi'])
            self.gridTransaksi.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.gridTransaksi.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.gridTransaksi.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            nomor_transaksi=self.txtNomorTransaksi.text()           
            tss = Transaksi()
            result = tss.getByKodeTrs(nomor_transaksi)
            a = tss.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNamaPelanggan.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False)
                self.btnHapus.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            tss = Transaksi()
            nomor_transaksi=self.txtNomorTransaksi.text()
            nama_pelanggan = self.txtNamaPelanggan.text()
            nomor_polisi = self.txtNomorPolisi.text()
            kode_pelayanan= self.txtKodePelayanan.text()
            waktu_pelayanan = self.txtWaktuPelayanan.time().toString("HH:mm:ss")
            waktu_selesai = self.txtWaktuSelesai.time().toString("HH:mm:ss")
            tanggal_transaksi = self.txtTanggalTransaksi.date().toString("yyyy-MM-dd")
            kode_service1 = self.txtKodeService1.text()
            kode_service2 = self.txtKodeService2.text()
            kode_service3 = self.txtKodeService3.text()
            total_biaya = self.txtTotalBiaya.text()
            uang_masuk = self.txtUangMasuk.text()
            uang_kembali = self.txtUangKembali.text()
            id_petugas = self.txtIDPetugas.text()
            if self.Lunas.isChecked():
                status_transaksi="Lunas"
            
            if self.Belum.isChecked():
                status_transaksi="Belum Bayar"
            
            if(self.edit_mode==False):   
                tss.nomor_transaksi = nomor_transaksi
                tss.nama_pelanggan = nama_pelanggan
                tss.nomor_polisi = nomor_polisi
                tss.kode_pelayanan = kode_pelayanan
                tss.waktu_pelayanan = waktu_pelayanan
                tss.waktu_selesai = waktu_selesai
                tss.tanggal_transaksi = tanggal_transaksi
                tss.kode_service1 = kode_service1
                tss.kode_service2 = kode_service2
                tss.kode_service3 = kode_service3
                tss.total_biaya = total_biaya
                tss.uang_masuk = uang_masuk
                tss.uang_kembali = uang_kembali
                tss.id_petugas = id_petugas
                tss.status_transaksi = status_transaksi
                a = tss.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Transaksi Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Transaksi Gagal Tersimpan")
                
                self.clear_entry(self)
                self.select_data()
            elif(self.edit_mode==True):
                tss.nomor_transaksi = nomor_transaksi
                tss.nama_pelanggan = nama_pelanggan
                tss.nomor_polisi = nomor_polisi
                tss.kode_pelayanan = kode_pelayanan
                tss.waktu_pelayanan = waktu_pelayanan
                tss.waktu_selesai = waktu_selesai
                tss.tanggal_transaksi = tanggal_transaksi
                tss.kode_service1 = kode_service1
                tss.kode_service2 = kode_service2
                tss.kode_service3 = kode_service3
                tss.total_biaya = total_biaya
                tss.uang_masuk = uang_masuk
                tss.uang_kembali = uang_kembali
                tss.id_petugas = id_petugas
                tss.status_transaksi = status_transaksi
                a = tss.updateByKodeTrs(nomor_transaksi)
                if(a>0):
                    self.messagebox("SUKSES", "Data Transaksi Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Transaksi Gagal Diperbarui")
                
                self.clear_entry(self)
                self.select_data()
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def delete_data(self, MainWindow):
        try:
            tss = Transaksi()
            nomor_transaksi=self.txtNomorTransaksi.text()
                       
            if(self.edit_mode==True):
                a = tss.deleteByKodeTrs(nomor_transaksi)
                if(a>0):
                    self.messagebox("SUKSES", "Data Transaksi Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Transaksi Gagal Dihapus")
                
                self.clear_entry(self)
                self.select_data()
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        self.txtNamaPelanggan.setText(result[2])
        self.txtNomorPolisi.setText(result[3])
        self.txtKodePelayanan.setText(result[4])
        self.cari_pelayanan()
        self.txtWaktuPelayanan.setTime(result[5])
        self.txtWaktuSelesai.setTime(result[6])
        self.txtTanggalTransaksi.setDate(result[7])
        self.txtKodeService1.setText(result[8])
        a=self.txtKodeService1.text()
        if(a!=""):
            self.cari_service1()
        self.txtKodeService2.setText(result[9])
        b = self.txtKodeService2.text()
        if(b!=""):
            self.cari_service2()
        self.txtKodeService3.setText(result[10])
        c = self.txtKodeService3.text()
        if(c!=""):
            self.cari_service3()
        self.txtTotalBiaya.setText(str(result[11]))
        self.cari_jumblah()
        self.txtUangMasuk.setText(str(result[12]))
        self.txtUangKembali.setText(str(result[13]))
        self.txtIDPetugas.setText(str(result[14]))
        self.cari_petugas()
        self.cari_hitungDuit()
        if(result[15]=="Lunas"):
            self.Lunas.setChecked(True)
            self.Belum.setChecked(False)
        else:
            self.Lunas.setChecked(False)
            self.Belum.setChecked(True)
        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.btnHapus.setEnabled(True)
        self.btnHapus.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;")

    def clear_entry(self, MainWindow):
        self.txtNomorTransaksi.setText("")
        self.txtNamaPelanggan.setText("")
        self.txtNomorPolisi.setText("")
        self.txtKodePelayanan.setText("")
        self.txtJasaPelayanan.setText("")
        self.txtKodeService1.setText("")
        self.txtJenisService1.setText("")
        self.txtHarga1.setText("")
        self.txtKodeService2.setText("")
        self.txtJenisService2.setText("")
        self.txtHarga2.setText("")
        self.txtKodeService3.setText("")
        self.txtJenisService3.setText("")
        self.txtHarga3.setText("")
        self.txtTotalBiaya.setText("")
        self.txtUangMasuk.setText("")
        self.txtUangKembali.setText("")
        self.txtIDPetugas.setText("")
        self.txtNamaPetugas.setText("")
        self.Lunas.setChecked(False)
        self.Belum.setChecked(False)
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

Trx = """ WindowLogin, MainBengkelKendaraan, WindowTransaksi, WindowPelayanan,  WindowPetugas, WindowService1 {
    border-image: url("icons/bengkel1.jpg") 0 0 0 0 stetch stretch; font-color: red; color: white; background-size: auto; background-position: center;
}"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowTransaksi()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowTransaksi()
    app.setStyleSheet(Trx)