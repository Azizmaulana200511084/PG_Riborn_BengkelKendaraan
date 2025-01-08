# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pelayanan.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1333, 717)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(330, 180, 141, 151))
        self.frame_4.setStyleSheet(u"border-image: url(\"ui/binkaibulet.png\") 0 0 0 0 stetch stretch;\n"
"border-radius: 50px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 20, 101, 111))
        self.frame_3.setStyleSheet(u"border-image: url(\"icons/icon.png\") 0 0 0 0 stetch stretch;\n"
"border-radius: 50px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(480, 140, 571, 361))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(124, 0, 0);\n"
"border-radius: 30px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame.setInputMethodHints(Qt.ImhNone)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(450, 40, 111, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background: transparent;")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 0, 211, 41))
        font2 = QFont()
        font2.setFamily(u"Script MT Bold")
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"background: transparent;\n"
"color: gold;")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 40, 101, 16))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background: transparent;")
        self.gridPelayanan = QTableWidget(self.frame)
        if (self.gridPelayanan.columnCount() < 5):
            self.gridPelayanan.setColumnCount(5)
        if (self.gridPelayanan.rowCount() < 10):
            self.gridPelayanan.setRowCount(10)
        self.gridPelayanan.setObjectName(u"gridPelayanan")
        self.gridPelayanan.setGeometry(QRect(20, 181, 541, 171))
        self.gridPelayanan.setStyleSheet(u"border: 2px solid gold;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"gridline-color: rgb(85, 255, 0);")
        self.gridPelayanan.setRowCount(10)
        self.gridPelayanan.setColumnCount(5)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(20, 60, 251, 21))
        self.frame_5.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.txtKodePelayanan = QLineEdit(self.frame_5)
        self.txtKodePelayanan.setObjectName(u"txtKodePelayanan")
        self.txtKodePelayanan.setGeometry(QRect(0, 0, 211, 20))
        self.txtKodePelayanan.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.btnCari = QPushButton(self.frame_5)
        self.btnCari.setObjectName(u"btnCari")
        self.btnCari.setGeometry(QRect(210, 0, 41, 21))
        font3 = QFont()
        font3.setPointSize(10)
        self.btnCari.setFont(font3)
        self.btnCari.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 150, 541, 31))
        self.frame_7.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.btnClear = QPushButton(self.frame_7)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(0, 0, 171, 31))
        self.btnClear.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.btnHapus = QPushButton(self.frame_7)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(370, 0, 171, 31))
        self.btnHapus.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.btnSimpan = QPushButton(self.frame_7)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(160, 0, 221, 31))
        self.btnSimpan.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.JenisKendaraan = QComboBox(self.frame)
        self.JenisKendaraan.addItem("")
        self.JenisKendaraan.addItem("")
        self.JenisKendaraan.addItem("")
        self.JenisKendaraan.setObjectName(u"JenisKendaraan")
        self.JenisKendaraan.setGeometry(QRect(300, 60, 261, 22))
        self.JenisKendaraan.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(20, 120, 251, 21))
        self.frame_8.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.ServiceBesar = QRadioButton(self.frame_8)
        self.ServiceBesar.setObjectName(u"ServiceBesar")
        self.ServiceBesar.setGeometry(QRect(140, 0, 111, 21))
        font4 = QFont()
        font4.setPointSize(8)
        self.ServiceBesar.setFont(font4)
        self.ServiceBesar.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.ServiceRingan = QRadioButton(self.frame_8)
        self.ServiceRingan.setObjectName(u"ServiceRingan")
        self.ServiceRingan.setGeometry(QRect(0, 0, 111, 21))
        self.ServiceRingan.setFont(font4)
        self.ServiceRingan.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 100, 101, 16))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"background: transparent;")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(300, 120, 261, 21))
        self.frame_6.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.btnCariIdService = QPushButton(self.frame_6)
        self.btnCariIdService.setObjectName(u"btnCariIdService")
        self.btnCariIdService.setGeometry(QRect(220, 0, 41, 21))
        self.btnCariIdService.setFont(font3)
        self.btnCariIdService.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.txtIDSERVICE = QLineEdit(self.frame_6)
        self.txtIDSERVICE.setObjectName(u"txtIDSERVICE")
        self.txtIDSERVICE.setGeometry(QRect(160, 0, 61, 20))
        font5 = QFont()
        font5.setPointSize(6)
        self.txtIDSERVICE.setFont(font5)
        self.txtIDSERVICE.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.txtJenisService = QLineEdit(self.frame_6)
        self.txtJenisService.setObjectName(u"txtJenisService")
        self.txtJenisService.setGeometry(QRect(0, 0, 161, 20))
        self.txtJenisService.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(490, 100, 71, 16))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background: transparent;")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(300, 140, 551, 361))
        self.frame_2.setStyleSheet(u"border-radius: 130px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(124, 0, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 230, 101, 41))
        font6 = QFont()
        font6.setFamily(u"Script MT Bold")
        font6.setPointSize(20)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"background: transparent;\n"
"color: gold;")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 260, 131, 41))
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"background: transparent;\n"
"color: gold;")
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 10, 211, 211))
        self.frame_9.setStyleSheet(u"border-image: url(\"icons/icon.png\") 0 0 0 0 stetch stretch;\n"
"border-radius: 50px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame_4.raise_()
        self.frame.raise_()
        self.frame_9.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Janis Kendaraan", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Data Pelayanan", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Kode Pelayanan", None))
        self.btnCari.setText(QCoreApplication.translate("MainWindow", u"cari", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btnHapus.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
        self.btnSimpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.JenisKendaraan.setItemText(0, "")
        self.JenisKendaraan.setItemText(1, QCoreApplication.translate("MainWindow", u"Sepeda Motor", None))
        self.JenisKendaraan.setItemText(2, QCoreApplication.translate("MainWindow", u"Mobil", None))

        self.ServiceBesar.setText(QCoreApplication.translate("MainWindow", u"Service Besar", None))
        self.ServiceRingan.setText(QCoreApplication.translate("MainWindow", u"Service Ringan", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Jasa Pelayanan", None))
        self.btnCariIdService.setText(QCoreApplication.translate("MainWindow", u"cari", None))
        self.txtIDSERVICE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Service", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ID Service", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Bengkel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Kendaraan", None))
    # retranslateUi

