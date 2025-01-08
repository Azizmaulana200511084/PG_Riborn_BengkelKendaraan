import sys
from GUI.Icons import get_icon
import psycopg2 as mc
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from forms.MainBengkelKendaraan import MainBengkelKendaraan
from classes.Petugas import Petugas as Login

qtcreator_file  = "ui/login.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowLogin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnSubmit.clicked.connect(self.app_login)

    def app_login(self):
        nama_petugas = self.txtNamaPetugas.text()
        pssword1 = self.txtPassword.text()
        valid = usr.Validasi(nama_petugas,pssword1)
        if(valid[0]==True):
            self.messagebox("info","Login Berhasil")
            if(valid[1]=='admin'):
                self.messagebox("Info", "Anda Login Sebagai Admin")
                dashboard.showFullScreen()
            if(valid[1]=='operator'):
                self.messagebox("Info", "Anda Login Sebagai Operator")
                dashboard.showFullScreen()
            if(valid[1]=='montir1'):
                self.messagebox("Info", "Anda Login Sebagai Montir 1")
                dashboard.showFullScreen()
            window.close()
        else:
            self.messagebox("info","Maaf Login Gagal")
    
    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setStyleSheet("QMessageBox, QPushButton, QLabel {background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.1 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0)); color: gold;}")
        mess.setWindowIcon(get_icon("icon"))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

Log = """ WindowLogin, MainBengkelKendaraan, WindowTransaksi, WindowPelayanan,  WindowPetugas, WindowService1 {
    border-image: url("icons/bengkel1.jpg") 0 0 0 0 stetch stretch; font-color: red; color: white; background-size: auto; background-position: center;
}"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowLogin()
    app.setStyleSheet(Log)
    dashboard = MainBengkelKendaraan()
    usr = Login ()
    sys.exit(app.exec_())
    
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowLogin()
    dashboard = MainBengkelKendaraan()
    app.setStyleSheet(Log)
    usr = Login()