# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'petugas.ui'
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
        MainWindow.resize(1332, 708)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(800, -140, 21, 821))
        self.frame.setStyleSheet(u"border-radius: 250px 30px;\n"
"float: left;\n"
"border: 8px solid qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(13, 39, 0), stop: 0.1 rgb(41, 115, 0), stop: 1.0 rgb(85, 255, 0));\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.1 rgb(41, 115, 0), stop: 1.0 rgb(13, 39, 0));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(830, 50, 501, 481))
        self.frame_2.setStyleSheet(u"border-radius: 250px 30px;\n"
"float: left;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: rgb(13, 39, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 70, 501, 411))
        self.frame_3.setStyleSheet(u"border-radius: 250px 30px;\n"
"float: left;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: rgb(11, 105, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 20, 181, 41))
        font = QFont()
        font.setFamily(u"Script MT Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"border: 2px solid transparent;\n"
"background: transparent;")
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(300, 20, 141, 41))
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"border: 2px solid transparent;\n"
"background: transparent;")
        self.btnSimpan = QPushButton(self.frame_3)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(0, 360, 501, 51))
        font1 = QFont()
        font1.setFamily(u"Script")
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnSimpan.setFont(font1)
        self.btnSimpan.setStyleSheet(u"\n"
"float: left;\n"
"border: 5px solid rgb(85,255,0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(190, 210, 121, 41))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"border: 2px solid transparent;")
        self.txtRolename = QLineEdit(self.frame_3)
        self.txtRolename.setObjectName(u"txtRolename")
        self.txtRolename.setGeometry(QRect(20, 250, 461, 51))
        font2 = QFont()
        font2.setPointSize(20)
        self.txtRolename.setFont(font2)
        self.txtRolename.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"text-align: center;\n"
"border-radius: 25px;\n"
"background-color: rgb(13, 39, 0);")
        self.txtRolename.setAlignment(Qt.AlignCenter)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 60, 231, 51))
        self.frame_4.setStyleSheet(u"border: 5px solid rgb(85, 255, 0);\n"
"background-color: rgb(13, 39, 0);\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 25px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.txtNamaUsers = QLineEdit(self.frame_4)
        self.txtNamaUsers.setObjectName(u"txtNamaUsers")
        self.txtNamaUsers.setGeometry(QRect(10, 10, 171, 31))
        self.txtNamaUsers.setFont(font2)
        self.txtNamaUsers.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"text-align: center;\n"
"border: 2px solid transparent;\n"
"border-radius: 25px;\n"
"background: transparent;")
        self.btnCari = QPushButton(self.frame_4)
        self.btnCari.setObjectName(u"btnCari")
        self.btnCari.setGeometry(QRect(180, 0, 51, 51))
        self.btnCari.setStyleSheet(u"border: 5px solid rgb(85, 255, 0);\n"
"background-color: rgb(13, 39, 0);\n"
"color: gold;\n"
"border-radius: 20px;")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(260, 60, 231, 51))
        self.frame_5.setStyleSheet(u"border: 5px solid rgb(85, 255, 0);\n"
"background-color: rgb(13, 39, 0);\n"
"color: rgb(85, 255, 0);\n"
"border-radius: 25px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.txtPsw = QLineEdit(self.frame_5)
        self.txtPsw.setObjectName(u"txtPsw")
        self.txtPsw.setGeometry(QRect(10, 10, 171, 31))
        self.txtPsw.setFont(font2)
        self.txtPsw.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"text-align: center;\n"
"border: 2px solid transparent;\n"
"border-radius: 25px;\n"
"background: transparent;")
        self.btnKodeUnik = QPushButton(self.frame_5)
        self.btnKodeUnik.setObjectName(u"btnKodeUnik")
        self.btnKodeUnik.setGeometry(QRect(180, 0, 51, 51))
        self.btnKodeUnik.setStyleSheet(u"border: 5px solid rgb(85, 255, 0);\n"
"background-color: rgb(13, 39, 0);\n"
"color: gold;\n"
"border-radius: 20px;")
        self.btnClear = QPushButton(self.frame_3)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(0, 320, 251, 51))
        self.btnClear.setFont(font1)
        self.btnClear.setStyleSheet(u"border-radius: 250px 20px;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.btnHapus = QPushButton(self.frame_3)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(240, 320, 261, 51))
        self.btnHapus.setFont(font1)
        self.btnHapus.setStyleSheet(u"border-radius: 250px 20px;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));\n"
"color: gold;")
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 120, 181, 41))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"border: 2px solid transparent;")
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(300, 120, 171, 41))
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"border: 2px solid transparent;")
        self.txtNoTelp = QLineEdit(self.frame_3)
        self.txtNoTelp.setObjectName(u"txtNoTelp")
        self.txtNoTelp.setGeometry(QRect(10, 160, 231, 51))
        self.txtNoTelp.setFont(font2)
        self.txtNoTelp.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"text-align: center;\n"
"border-radius: 25px;\n"
"background-color: rgb(13, 39, 0);")
        self.txtNoTelp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txtEmailPtg = QLineEdit(self.frame_3)
        self.txtEmailPtg.setObjectName(u"txtEmailPtg")
        self.txtEmailPtg.setGeometry(QRect(260, 160, 231, 51))
        self.txtEmailPtg.setFont(font2)
        self.txtEmailPtg.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"text-align: center;\n"
"border-radius: 25px;\n"
"background-color: rgb(13, 39, 0);")
        self.txtEmailPtg.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btnHapus.raise_()
        self.btnClear.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.btnSimpan.raise_()
        self.label_18.raise_()
        self.txtRolename.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.txtNoTelp.raise_()
        self.txtEmailPtg.raise_()
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(180, 10, 151, 61))
        font3 = QFont()
        font3.setFamily(u"Script MT Bold")
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.label_12.setFont(font3)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;\n"
"color: gold;")
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(60, 190, 671, 331))
        self.frame_6.setStyleSheet(u"border-radius: 250px 30px;\n"
"float: left;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color:qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridPetugas = QTableWidget(self.frame_6)
        if (self.gridPetugas.columnCount() < 6):
            self.gridPetugas.setColumnCount(6)
        if (self.gridPetugas.rowCount() < 10):
            self.gridPetugas.setRowCount(10)
        self.gridPetugas.setObjectName(u"gridPetugas")
        self.gridPetugas.setGeometry(QRect(10, 30, 651, 291))
        font4 = QFont()
        font4.setPointSize(10)
        self.gridPetugas.setFont(font4)
        self.gridPetugas.setStyleSheet(u"border: 2px solid rgb(85, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"gridline-color: rgb(85, 255, 0);")
        self.gridPetugas.setGridStyle(Qt.SolidLine)
        self.gridPetugas.setRowCount(10)
        self.gridPetugas.setColumnCount(6)
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(60, 490, 671, 41))
        self.frame_7.setStyleSheet(u"border-radius: 40px 10px;\n"
"float: left;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(60, 180, 671, 41))
        self.frame_8.setStyleSheet(u"border-radius: 40px 10px;\n"
"float: left;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(730, 170, 21, 61))
        self.frame_9.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.centralwidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(40, 170, 21, 61))
        self.frame_10.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.centralwidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(730, 480, 21, 61))
        self.frame_11.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.centralwidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(40, 480, 21, 61))
        self.frame_12.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_16 = QFrame(self.centralwidget)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(750, 490, 21, 41))
        self.frame_16.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_17 = QFrame(self.centralwidget)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(20, 180, 21, 41))
        self.frame_17.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_18 = QFrame(self.centralwidget)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(750, 180, 21, 41))
        self.frame_18.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_19 = QFrame(self.centralwidget)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(20, 490, 21, 41))
        self.frame_19.setStyleSheet(u"border-radius: 8;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.centralwidget)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(770, 190, 21, 21))
        self.frame_20.setStyleSheet(u"border-radius: 10;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_21 = QFrame(self.centralwidget)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(0, 190, 21, 21))
        self.frame_21.setStyleSheet(u"border-radius: 10;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.frame_22 = QFrame(self.centralwidget)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(0, 500, 21, 21))
        self.frame_22.setStyleSheet(u"border-radius: 10;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_23 = QFrame(self.centralwidget)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(770, 500, 21, 21))
        self.frame_23.setStyleSheet(u"border-radius: 10;\n"
"border: 5px solid rgb(85, 255, 0);\n"
"background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 0.8 rgb(41, 115, 0), stop: 1.0 rgb(41, 115, 0));")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(290, 180, 241, 41))
        font5 = QFont()
        font5.setFamily(u"Script MT Bold")
        font5.setPointSize(25)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.label_13.setFont(font5)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet(u"border: 2px solid transparent;\n"
"background: transparent;\n"
"color: gold;")
        self.frame_13 = QFrame(self.centralwidget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(320, 20, 151, 141))
        self.frame_13.setStyleSheet(u"border-image: url(\"icons/icon.png\") 0 0 0 0 stetch stretch;\n"
"border-radius: 50px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_6.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_8.raise_()
        self.frame_9.raise_()
        self.frame_10.raise_()
        self.frame_11.raise_()
        self.frame_12.raise_()
        self.frame_16.raise_()
        self.frame_17.raise_()
        self.frame_18.raise_()
        self.frame_19.raise_()
        self.frame_20.raise_()
        self.frame_21.raise_()
        self.frame_22.raise_()
        self.frame_23.raise_()
        self.label_13.raise_()
        self.frame_13.raise_()
        self.frame_7.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nama Petugas", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Kata Sandi", None))
        self.btnSimpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Rolename", None))
        self.btnCari.setText(QCoreApplication.translate("MainWindow", u"cari", None))
        self.btnKodeUnik.setText(QCoreApplication.translate("MainWindow", u"MD5", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btnHapus.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Nomor Telepon", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Email Petugas", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Data Petugas", None))
    # retranslateUi

