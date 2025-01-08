# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transaksi.ui'
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
        MainWindow.resize(1333, 722)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 40, 1241, 521))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(124, 0, 0);\n"
"border-radius: 30px;\n"
"border: 2px solid gold;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.1 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame.setInputMethodHints(Qt.ImhNone)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 60, 1221, 351))
        self.frame_2.setFont(font)
        self.frame_2.setLayoutDirection(Qt.LeftToRight)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"border-radius: 30px;")
        self.frame_2.setInputMethodHints(Qt.ImhNone)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 90, 161, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;")
        self.txtTanggalTransaksi = QDateEdit(self.frame_2)
        self.txtTanggalTransaksi.setObjectName(u"txtTanggalTransaksi")
        self.txtTanggalTransaksi.setGeometry(QRect(190, 160, 331, 21))
        self.txtTanggalTransaksi.setFont(font1)
        self.txtTanggalTransaksi.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.txtTanggalTransaksi.setDateTime(QDateTime(QDate(2022, 9, 14), QTime(0, 0, 0)))
        self.txtTanggalTransaksi.setMinimumDate(QDate(2022, 1, 1))
        self.txtTanggalTransaksi.setCalendarPopup(True)
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 60, 111, 31))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;")
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 10, 131, 20))
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;")
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 150, 171, 41))
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;")
        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(690, 100, 111, 21))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;")
        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(690, 40, 111, 21))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;")
        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(690, 70, 111, 21))
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(540, 30, 141, 151))
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
        self.txtNamaPelanggan = QLineEdit(self.frame_2)
        self.txtNamaPelanggan.setObjectName(u"txtNamaPelanggan")
        self.txtNamaPelanggan.setGeometry(QRect(190, 40, 331, 20))
        self.txtNamaPelanggan.setFont(font1)
        self.txtNamaPelanggan.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 30, 131, 31))
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;")
        self.txtNomorPolisi = QLineEdit(self.frame_2)
        self.txtNomorPolisi.setObjectName(u"txtNomorPolisi")
        self.txtNomorPolisi.setGeometry(QRect(190, 70, 331, 20))
        self.txtNomorPolisi.setFont(font1)
        self.txtNomorPolisi.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(690, 120, 121, 41))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;")
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 220, 1221, 31))
        self.frame_7.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.btnClear = QPushButton(self.frame_7)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(0, 0, 341, 31))
        self.btnClear.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.btnHapus = QPushButton(self.frame_7)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(880, 0, 341, 31))
        self.btnHapus.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.btnSimpan = QPushButton(self.frame_7)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(310, 0, 601, 31))
        self.btnSimpan.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(190, 10, 331, 21))
        self.frame_12.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.btnCari = QPushButton(self.frame_12)
        self.btnCari.setObjectName(u"btnCari")
        self.btnCari.setGeometry(QRect(290, 0, 41, 23))
        font2 = QFont()
        font2.setPointSize(10)
        self.btnCari.setFont(font2)
        self.btnCari.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.txtNomorTransaksi = QLineEdit(self.frame_12)
        self.txtNomorTransaksi.setObjectName(u"txtNomorTransaksi")
        self.txtNomorTransaksi.setGeometry(QRect(0, 0, 291, 20))
        self.txtNomorTransaksi.setFont(font1)
        self.txtNomorTransaksi.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(810, 40, 401, 21))
        self.frame_13.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.btnCariKodeService1 = QToolButton(self.frame_13)
        self.btnCariKodeService1.setObjectName(u"btnCariKodeService1")
        self.btnCariKodeService1.setGeometry(QRect(370, 0, 31, 21))
        self.btnCariKodeService1.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.txtJenisService1 = QLineEdit(self.frame_13)
        self.txtJenisService1.setObjectName(u"txtJenisService1")
        self.txtJenisService1.setGeometry(QRect(0, 0, 191, 21))
        self.txtJenisService1.setFont(font1)
        self.txtJenisService1.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.txtKodeService1 = QLineEdit(self.frame_13)
        self.txtKodeService1.setObjectName(u"txtKodeService1")
        self.txtKodeService1.setGeometry(QRect(300, 0, 71, 21))
        self.txtKodeService1.setFont(font1)
        self.txtKodeService1.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_22 = QFrame(self.frame_13)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(190, 0, 111, 21))
        self.frame_22.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.label_36 = QLabel(self.frame_22)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(0, 0, 41, 21))
        self.label_36.setFont(font1)
        self.label_36.setStyleSheet(u"padding: 0 8px;\n"
"color: gold;\n"
"border: transparent;\n"
"background: transparent;")
        self.txtHarga1 = QLineEdit(self.frame_22)
        self.txtHarga1.setObjectName(u"txtHarga1")
        self.txtHarga1.setGeometry(QRect(30, 0, 81, 21))
        self.txtHarga1.setFont(font1)
        self.txtHarga1.setStyleSheet(u"padding: 0 8px;\n"
"color: gold;\n"
"border: transparent;\n"
"background: transparent;")
        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(810, 70, 401, 21))
        self.frame_15.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.btnCariKodeService2 = QToolButton(self.frame_15)
        self.btnCariKodeService2.setObjectName(u"btnCariKodeService2")
        self.btnCariKodeService2.setGeometry(QRect(370, 0, 31, 21))
        self.btnCariKodeService2.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.txtJenisService2 = QLineEdit(self.frame_15)
        self.txtJenisService2.setObjectName(u"txtJenisService2")
        self.txtJenisService2.setGeometry(QRect(0, 0, 191, 21))
        self.txtJenisService2.setFont(font1)
        self.txtJenisService2.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.txtKodeService2 = QLineEdit(self.frame_15)
        self.txtKodeService2.setObjectName(u"txtKodeService2")
        self.txtKodeService2.setGeometry(QRect(300, 0, 71, 21))
        self.txtKodeService2.setFont(font1)
        self.txtKodeService2.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_23 = QFrame(self.frame_15)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(190, 0, 111, 21))
        self.frame_23.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.label_37 = QLabel(self.frame_23)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(0, 0, 41, 21))
        self.label_37.setFont(font1)
        self.label_37.setStyleSheet(u"padding: 0 8px;\n"
"color: gold;\n"
"border: transparent;\n"
"background: transparent;")
        self.txtHarga2 = QLineEdit(self.frame_23)
        self.txtHarga2.setObjectName(u"txtHarga2")
        self.txtHarga2.setGeometry(QRect(30, 0, 81, 21))
        self.txtHarga2.setFont(font1)
        self.txtHarga2.setStyleSheet(u"padding: 0 8px;\n"
"color: gold;\n"
"border: transparent;\n"
"background: transparent;")
        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(810, 100, 401, 21))
        self.frame_16.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.btnCariKodeService3 = QToolButton(self.frame_16)
        self.btnCariKodeService3.setObjectName(u"btnCariKodeService3")
        self.btnCariKodeService3.setGeometry(QRect(370, 0, 31, 21))
        self.btnCariKodeService3.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.txtJenisService3 = QLineEdit(self.frame_16)
        self.txtJenisService3.setObjectName(u"txtJenisService3")
        self.txtJenisService3.setGeometry(QRect(0, 0, 191, 21))
        self.txtJenisService3.setFont(font1)
        self.txtJenisService3.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.txtKodeService3 = QLineEdit(self.frame_16)
        self.txtKodeService3.setObjectName(u"txtKodeService3")
        self.txtKodeService3.setGeometry(QRect(300, 0, 71, 21))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.txtKodeService3.setFont(font3)
        self.txtKodeService3.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_24 = QFrame(self.frame_16)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(190, 0, 111, 21))
        self.frame_24.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.label_38 = QLabel(self.frame_24)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(0, 0, 41, 21))
        self.label_38.setFont(font1)
        self.label_38.setStyleSheet(u"padding: 0 8px;\n"
"color: gold;\n"
"border: transparent;\n"
"background: transparent;")
        self.txtHarga3 = QLineEdit(self.frame_24)
        self.txtHarga3.setObjectName(u"txtHarga3")
        self.txtHarga3.setGeometry(QRect(30, 0, 81, 21))
        self.txtHarga3.setFont(font1)
        self.txtHarga3.setStyleSheet(u"padding: 0 8px;\n"
"color: gold;\n"
"border: transparent;\n"
"background: transparent;")
        self.frame_18 = QFrame(self.frame_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(810, 130, 401, 21))
        self.frame_18.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.btnCariJumblah = QToolButton(self.frame_18)
        self.btnCariJumblah.setObjectName(u"btnCariJumblah")
        self.btnCariJumblah.setGeometry(QRect(300, 0, 101, 21))
        self.btnCariJumblah.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.txtTotalBiaya = QLineEdit(self.frame_18)
        self.txtTotalBiaya.setObjectName(u"txtTotalBiaya")
        self.txtTotalBiaya.setGeometry(QRect(0, 0, 301, 20))
        self.txtTotalBiaya.setFont(font1)
        self.txtTotalBiaya.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(190, 100, 331, 21))
        self.frame_14.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.btnCariKodePelayanan = QToolButton(self.frame_14)
        self.btnCariKodePelayanan.setObjectName(u"btnCariKodePelayanan")
        self.btnCariKodePelayanan.setGeometry(QRect(260, 0, 71, 21))
        font4 = QFont()
        font4.setPointSize(8)
        self.btnCariKodePelayanan.setFont(font4)
        self.btnCariKodePelayanan.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.txtKodePelayanan = QLineEdit(self.frame_14)
        self.txtKodePelayanan.setObjectName(u"txtKodePelayanan")
        self.txtKodePelayanan.setGeometry(QRect(0, 0, 261, 20))
        self.txtKodePelayanan.setFont(font1)
        self.txtKodePelayanan.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_19 = QFrame(self.frame_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(10, 130, 231, 21))
        self.frame_19.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_19)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 0, 101, 21))
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;\n"
"color: black;")
        self.txtWaktuPelayanan = QTimeEdit(self.frame_19)
        self.txtWaktuPelayanan.setObjectName(u"txtWaktuPelayanan")
        self.txtWaktuPelayanan.setGeometry(QRect(150, 0, 81, 21))
        self.txtWaktuPelayanan.setFont(font4)
        self.txtWaktuPelayanan.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_21 = QFrame(self.frame_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(300, 130, 221, 21))
        self.frame_21.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.label_30 = QLabel(self.frame_21)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(0, 0, 81, 21))
        self.label_30.setFont(font4)
        self.label_30.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;\n"
"color: black;")
        self.txtWaktuSelesai = QTimeEdit(self.frame_21)
        self.txtWaktuSelesai.setObjectName(u"txtWaktuSelesai")
        self.txtWaktuSelesai.setGeometry(QRect(140, 0, 81, 21))
        self.txtWaktuSelesai.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_20 = QFrame(self.frame_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(0, 190, 1221, 41))
        self.frame_20.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame_20)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(100, -1, 1011, 41))
        self.frame_11.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.btnCariKembalian = QToolButton(self.frame_11)
        self.btnCariKembalian.setObjectName(u"btnCariKembalian")
        self.btnCariKembalian.setGeometry(QRect(210, 0, 601, 31))
        self.btnCariKembalian.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.label_34 = QLabel(self.frame_11)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(0, 0, 41, 31))
        self.label_34.setFont(font1)
        self.label_34.setStyleSheet(u"padding: 0 8px;\n"
"color: gold;\n"
"border: transparent;\n"
"background: transparent;")
        self.txtUangMasuk = QLineEdit(self.frame_11)
        self.txtUangMasuk.setObjectName(u"txtUangMasuk")
        self.txtUangMasuk.setGeometry(QRect(30, 0, 181, 31))
        self.txtUangMasuk.setFont(font1)
        self.txtUangMasuk.setStyleSheet(u"padding: 0 8px;\n"
"color: gold;\n"
"border: transparent;\n"
"background: transparent;")
        self.label_35 = QLabel(self.frame_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(810, 0, 41, 31))
        self.label_35.setFont(font1)
        self.label_35.setStyleSheet(u"padding: 0 8px;\n"
"color: gold;\n"
"border: transparent;\n"
"background: transparent;")
        self.txtUangKembali = QLineEdit(self.frame_11)
        self.txtUangKembali.setObjectName(u"txtUangKembali")
        self.txtUangKembali.setGeometry(QRect(840, 0, 171, 31))
        self.txtUangKembali.setFont(font1)
        self.txtUangKembali.setStyleSheet(u"padding: 0 8px;\n"
"color: gold;\n"
"border: transparent;\n"
"background: transparent;")
        self.label_32 = QLabel(self.frame_20)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(0, 0, 101, 31))
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;\n"
"color: black;")
        self.label_33 = QLabel(self.frame_20)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(1110, 0, 111, 31))
        self.label_33.setFont(font1)
        self.label_33.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;\n"
"color: black;")
        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(810, 10, 401, 21))
        self.frame_17.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.btnCariIDPetugas = QToolButton(self.frame_17)
        self.btnCariIDPetugas.setObjectName(u"btnCariIDPetugas")
        self.btnCariIDPetugas.setGeometry(QRect(300, 0, 101, 21))
        self.btnCariIDPetugas.setFont(font2)
        self.btnCariIDPetugas.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.txtIDPetugas = QLineEdit(self.frame_17)
        self.txtIDPetugas.setObjectName(u"txtIDPetugas")
        self.txtIDPetugas.setGeometry(QRect(0, 0, 301, 20))
        self.txtIDPetugas.setFont(font1)
        self.txtIDPetugas.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(690, 0, 91, 41))
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;")
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(810, 160, 401, 21))
        self.frame_8.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.Lunas = QRadioButton(self.frame_8)
        self.Lunas.setObjectName(u"Lunas")
        self.Lunas.setGeometry(QRect(0, 0, 82, 21))
        font5 = QFont()
        font5.setPointSize(9)
        self.Lunas.setFont(font5)
        self.Lunas.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.Belum = QRadioButton(self.frame_8)
        self.Belum.setObjectName(u"Belum")
        self.Belum.setGeometry(QRect(300, 0, 101, 21))
        self.Belum.setFont(font4)
        self.Belum.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(690, 150, 121, 41))
        font6 = QFont()
        font6.setPointSize(11)
        self.label_22.setFont(font6)
        self.label_22.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;")
        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(520, 0, 171, 31))
        font7 = QFont()
        font7.setFamily(u"Script MT Bold")
        font7.setPointSize(15)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_26.setFont(font7)
        self.label_26.setStyleSheet(u"color: gold;\n"
"border: 2px solid transparent;\n"
"background: transparent;")
        self.frame_20.raise_()
        self.frame_7.raise_()
        self.label_12.raise_()
        self.txtTanggalTransaksi.raise_()
        self.label_16.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.frame_4.raise_()
        self.txtNamaPelanggan.raise_()
        self.label_17.raise_()
        self.txtNomorPolisi.raise_()
        self.label_31.raise_()
        self.frame_12.raise_()
        self.frame_13.raise_()
        self.frame_15.raise_()
        self.frame_16.raise_()
        self.frame_18.raise_()
        self.frame_14.raise_()
        self.frame_19.raise_()
        self.frame_21.raise_()
        self.frame_17.raise_()
        self.label_25.raise_()
        self.frame_8.raise_()
        self.label_22.raise_()
        self.label_26.raise_()
        self.gridTransaksi = QTableWidget(self.frame)
        if (self.gridTransaksi.columnCount() < 16):
            self.gridTransaksi.setColumnCount(16)
        if (self.gridTransaksi.rowCount() < 10):
            self.gridTransaksi.setRowCount(10)
        self.gridTransaksi.setObjectName(u"gridTransaksi")
        self.gridTransaksi.setGeometry(QRect(0, 310, 1241, 192))
        self.gridTransaksi.setFont(font4)
        self.gridTransaksi.setStyleSheet(u"border: 2px solid gold;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"gridline-color: rgb(85, 255, 0);")
        self.gridTransaksi.setRowCount(10)
        self.gridTransaksi.setColumnCount(16)
        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(900, 20, 271, 31))
        font8 = QFont()
        font8.setPointSize(15)
        self.label_27.setFont(font8)
        self.label_27.setStyleSheet(u"border: 2px solid transparent;")
        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 20, 161, 31))
        self.label_28.setFont(font8)
        self.label_28.setStyleSheet(u"border: 2px solid transparent;")
        self.txtNamaPetugas = QLineEdit(self.frame)
        self.txtNamaPetugas.setObjectName(u"txtNamaPetugas")
        self.txtNamaPetugas.setGeometry(QRect(1100, 20, 121, 31))
        self.txtNamaPetugas.setFont(font8)
        self.txtNamaPetugas.setStyleSheet(u"color: gold;\n"
"border: 2px solid transparent;")
        self.txtJasaPelayanan = QLineEdit(self.frame)
        self.txtJasaPelayanan.setObjectName(u"txtJasaPelayanan")
        self.txtJasaPelayanan.setGeometry(QRect(180, 20, 171, 31))
        self.txtJasaPelayanan.setFont(font8)
        self.txtJasaPelayanan.setStyleSheet(u"color: gold;\n"
"border: 2px solid transparent;")
        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(480, 0, 271, 51))
        font9 = QFont()
        font9.setFamily(u"Script MT Bold")
        font9.setPointSize(30)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setWeight(75)
        self.label_29.setFont(font9)
        self.label_29.setAutoFillBackground(False)
        self.label_29.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;\n"
"color: gold;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Kode Pelayanan", None))
        self.txtTanggalTransaksi.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nomor Polisi", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Nomor Transaksi", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tanggal Transaksi", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Kode Service3", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Kode Service1", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Kode Service2", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Nama Pelanggan", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Total Biaya", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btnHapus.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
        self.btnSimpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.btnCari.setText(QCoreApplication.translate("MainWindow", u"cari", None))
        self.btnCariKodeService1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.txtKodeService1.setText("")
        self.txtKodeService1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kode1", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"RP", None))
        self.btnCariKodeService2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.txtKodeService2.setText("")
        self.txtKodeService2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kode2", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"RP", None))
        self.btnCariKodeService3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.txtKodeService3.setText("")
        self.txtKodeService3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kode3", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"RP", None))
        self.btnCariJumblah.setText(QCoreApplication.translate("MainWindow", u"Jumblah Biaya", None))
        self.btnCariKodePelayanan.setText(QCoreApplication.translate("MainWindow", u"Pencarian", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Waktu Pelayanan", None))
        self.txtWaktuPelayanan.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Waktu Selesai", None))
        self.txtWaktuSelesai.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.btnCariKembalian.setText(QCoreApplication.translate("MainWindow", u"Hitung Kembalian", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"RP", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"RP", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Uang Masuk", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Uang Kembali", None))
        self.btnCariIDPetugas.setText(QCoreApplication.translate("MainWindow", u"Cari Petugas", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"ID Petugas", None))
        self.Lunas.setText(QCoreApplication.translate("MainWindow", u"Lunas", None))
        self.Belum.setText(QCoreApplication.translate("MainWindow", u"Belum Bayar", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Status Transaksi", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Bengkel Kendaraan", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Nama Petugas Dari :", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Jasa Pelayanan :", None))
        self.txtNamaPetugas.setText("")
        self.txtJasaPelayanan.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Data Transaksi", None))
    # retranslateUi

