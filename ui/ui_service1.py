# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'service1.ui'
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
        MainWindow.resize(1350, 722)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(410, 140, 561, 391))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(124, 0, 0);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.5 rgb(41, 115, 0), stop: 0.5 rgb(41, 115, 0));")
        self.frame.setInputMethodHints(Qt.ImhNone)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 60, 541, 311))
        self.frame_5.setFont(font)
        self.frame_5.setLayoutDirection(Qt.LeftToRight)
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 1.1 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"border-radius: 30px;")
        self.frame_5.setInputMethodHints(Qt.ImhNone)
        self.label_27 = QLabel(self.frame_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 70, 61, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"background: transparent;\n"
"border: transparent;\n"
"color: gold;")
        self.txtJenisService = QLineEdit(self.frame_5)
        self.txtJenisService.setObjectName(u"txtJenisService")
        self.txtJenisService.setGeometry(QRect(120, 50, 181, 20))
        font2 = QFont()
        font2.setPointSize(12)
        self.txtJenisService.setFont(font2)
        self.txtJenisService.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.label_29 = QLabel(self.frame_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 40, 111, 31))
        self.label_29.setFont(font1)
        self.label_29.setStyleSheet(u"background: transparent;\n"
"border: transparent;\n"
"color: gold;")
        self.txtHarga = QLineEdit(self.frame_5)
        self.txtHarga.setObjectName(u"txtHarga")
        self.txtHarga.setGeometry(QRect(120, 80, 181, 20))
        self.txtHarga.setFont(font2)
        self.txtHarga.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 20, 111, 20))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"background: transparent;\n"
"border: transparent;\n"
"color: gold;")
        self.btnClear = QPushButton(self.frame_5)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(120, 140, 75, 21))
        self.btnClear.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: gold;\n"
"color: rgb(0, 0, 0);")
        self.txtMerek = QLineEdit(self.frame_5)
        self.txtMerek.setObjectName(u"txtMerek")
        self.txtMerek.setGeometry(QRect(120, 110, 181, 21))
        self.txtMerek.setFont(font2)
        self.txtMerek.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.label_35 = QLabel(self.frame_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 100, 61, 31))
        self.label_35.setFont(font1)
        self.label_35.setStyleSheet(u"background: transparent;\n"
"border: transparent;\n"
"color: gold;")
        self.btnSimpan = QPushButton(self.frame_5)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 140, 75, 21))
        self.btnSimpan.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: gold;\n"
"color: rgb(0, 0, 0);")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(370, 10, 141, 151))
        self.frame_6.setStyleSheet(u"border-image: url(\"ui/binkaibulet.png\") 0 0 0 0 stetch stretch;\n"
"border-radius: 50px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 20, 101, 111))
        self.frame_7.setStyleSheet(u"border-image: url(\"icons/icon.png\") 0 0 0 0 stetch stretch;\n"
"border-radius: 50px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.btnHapus = QPushButton(self.frame_5)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(230, 140, 75, 21))
        self.btnHapus.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: gold;\n"
"color: rgb(0, 0, 0);")
        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(120, 21, 181, 20))
        self.frame_14.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: gold;\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 10px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.txtKodeSV = QLineEdit(self.frame_14)
        self.txtKodeSV.setObjectName(u"txtKodeSV")
        self.txtKodeSV.setGeometry(QRect(0, 0, 141, 20))
        self.txtKodeSV.setFont(font2)
        self.txtKodeSV.setStyleSheet(u"border: 2px solid gold;\n"
"background-color: rgb(13, 39, 0);\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"color: gold;")
        self.btnCari = QPushButton(self.frame_14)
        self.btnCari.setObjectName(u"btnCari")
        self.btnCari.setGeometry(QRect(140, 0, 41, 21))
        font3 = QFont()
        font3.setPointSize(10)
        self.btnCari.setFont(font3)
        self.btnCari.setStyleSheet(u"border: 2px solid goldenrod;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.4 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.gridService1 = QTableWidget(self.frame)
        if (self.gridService1.columnCount() < 5):
            self.gridService1.setColumnCount(5)
        if (self.gridService1.rowCount() < 10):
            self.gridService1.setRowCount(10)
        self.gridService1.setObjectName(u"gridService1")
        self.gridService1.setGeometry(QRect(0, 230, 561, 141))
        self.gridService1.setFont(font3)
        self.gridService1.setStyleSheet(u"border: 2px solid gold;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"gridline-color: rgb(85, 255, 0);")
        self.gridService1.setRowCount(10)
        self.gridService1.setColumnCount(5)
        self.label_41 = QLabel(self.frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(130, 10, 301, 51))
        font4 = QFont()
        font4.setFamily(u"Script MT Bold")
        font4.setPointSize(30)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.label_41.setFont(font4)
        self.label_41.setAutoFillBackground(False)
        self.label_41.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;\n"
"color: gold;")
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(930, 120, 61, 21))
        self.frame_9.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.centralwidget)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(950, 80, 21, 21))
        self.frame_20.setStyleSheet(u"border-radius: 10;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_18 = QFrame(self.centralwidget)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(940, 100, 41, 21))
        self.frame_18.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(940, 130, 41, 411))
        self.frame_8.setStyleSheet(u"border-radius: 10px 40px;\n"
"float: left;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.5 rgb(41, 115, 0), stop: 0.5 rgb(41, 115, 0));")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.centralwidget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(400, 130, 41, 411))
        self.frame_13.setStyleSheet(u"border-radius: 10px 40px;\n"
"float: left;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.5 rgb(41, 115, 0), stop: 0.5 rgb(41, 115, 0));")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.centralwidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(390, 120, 61, 21))
        self.frame_10.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_21 = QFrame(self.centralwidget)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(410, 80, 21, 21))
        self.frame_21.setStyleSheet(u"border-radius: 10;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.frame_24 = QFrame(self.centralwidget)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(400, 100, 41, 21))
        self.frame_24.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.centralwidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(940, 530, 41, 16))
        self.frame_11.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_15 = QFrame(self.centralwidget)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(930, 540, 61, 16))
        self.frame_15.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_17 = QFrame(self.centralwidget)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(920, 550, 81, 16))
        self.frame_17.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_25 = QFrame(self.centralwidget)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(390, 540, 61, 16))
        self.frame_25.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.frame_26 = QFrame(self.centralwidget)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(380, 550, 81, 16))
        self.frame_26.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.frame_27 = QFrame(self.centralwidget)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(400, 530, 41, 16))
        self.frame_27.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.frame_28 = QFrame(self.centralwidget)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(520, 100, 341, 31))
        self.frame_28.setStyleSheet(u"border-radius: 13;\n"
"border: 2px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.centralwidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(490, 120, 401, 31))
        self.frame_12.setStyleSheet(u"border-radius: 13;\n"
"border: 2px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_29 = QFrame(self.centralwidget)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(490, 30, 401, 431))
        self.frame_29.setStyleSheet(u"border-radius: 200;\n"
"border: 15px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 1 rgb(85, 255, 0), stop: 1.2 rgb(41, 115, 0), stop: 0.9 rgb(41, 115, 0));")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.frame_16 = QFrame(self.centralwidget)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(10, 10, 211, 211))
        self.frame_16.setStyleSheet(u"border-image: url(\"icons/icon.png\") 0 0 0 0 stetch stretch;\n"
"border-radius: 50px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_29.raise_()
        self.frame_28.raise_()
        self.frame_12.raise_()
        self.frame_13.raise_()
        self.frame_8.raise_()
        self.frame.raise_()
        self.frame_9.raise_()
        self.frame_20.raise_()
        self.frame_18.raise_()
        self.frame_10.raise_()
        self.frame_21.raise_()
        self.frame_24.raise_()
        self.frame_17.raise_()
        self.frame_15.raise_()
        self.frame_11.raise_()
        self.frame_26.raise_()
        self.frame_25.raise_()
        self.frame_27.raise_()
        self.frame_16.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Harga", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Jenis Service", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Kode Service", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Merek", None))
        self.btnSimpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
        self.btnCari.setText(QCoreApplication.translate("MainWindow", u"cari", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"# Data Service #", None))
    # retranslateUi

