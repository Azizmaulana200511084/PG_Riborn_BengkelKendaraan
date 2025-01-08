from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmPetugas import WindowPetugas
from forms.frmPelayanan import WindowPelayanan
from forms.frmService1 import WindowService1
from forms.frmTransaksi import WindowTransaksi
dock = QtWidgets.QDockWidget()
def child_panels(self):
    petugas_panel(self)
    pelayanan_panel(self)
    service1_panel(self)
    transaksi_panel(self)

def petugas_panel(self):     
    petugas_widget = WindowPetugas()
    petugas_widget.select_data()
    self.centralwidget = petugas_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)
        

def pelayanan_panel(self):
    pelayanan_widget = WindowPelayanan()
    pelayanan_widget.select_data()
    self.centralwidget = pelayanan_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def service1_panel(self):
    service1_widget = WindowService1()
    service1_widget.select_data()
    self.centralwidget = service1_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def transaksi_panel(self):
    transaksi_widget = WindowTransaksi()
    transaksi_widget.select_data()
    self.centralwidget = transaksi_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def petugas_on(self):
    petugas_widget = WindowPetugas()
    petugas_widget.select_data()
    self.centralwidget = petugas_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def pelayanan_on(self):
    pelayanan_widget = WindowPelayanan()
    pelayanan_widget.select_data()
    self.centralwidget = pelayanan_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def service1_on(self):
    service1_widget = WindowService1()
    service1_widget.select_data()
    self.centralwidget = service1_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def transaksi_on(self):
    transaksi_widget = WindowTransaksi()
    transaksi_widget.select_data()
    self.centralwidget = transaksi_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()




        
     