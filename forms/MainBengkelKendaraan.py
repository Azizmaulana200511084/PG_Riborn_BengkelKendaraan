from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence as QKSec
from GUI.RibbonButton import RibbonButton
from GUI.Icons import get_icon
from GUI.RibbonTextbox import RibbonTextbox
from GUI.RibbonWidget import *
from panel.Panel import *
import sys

class MainBengkelKendaraan(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.resize(1280, 800)
        self.setWindowTitle("Kelompok 7")
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("icon"))
        child_panels(self)
 
        # -------------      actions       -----------------

        self._petugas_action = self.add_action("Petugas", "petugas", "Data Petugas", True, self.on_petugas)
        self._pelayanan_action = self.add_action("Pelayanan", "pelayanan", "Data Pelayanan", True, self.on_pelayanan)
        self._service1_action = self.add_action("Service", "service1", "Data Service1", True, self.on_service1)
        self._transaksi_action = self.add_action("Transaksi", "transaksi", "Data Transaksi", True, self.on_transaksi)
        self._zoom_action = self.add_action("Search", "zoom", "Search", True, self.on_zoom)
        self._about_action = self.add_action("About", "about", "About QupyRibbon", True, self.on_about)
        self._license_action = self.add_action("License", "license", "Licence for this software", True, self.on_license)
        self._exit_action = self.add_action("Exit", "exit", "Exit", True, self.app_exit)

        # Ribbon

        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)
        self.init_ribbon()

    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action

    def init_ribbon(self):
        home_tab = self._ribbon.add_ribbon_tab("Home")
        file_pane = home_tab.add_ribbon_pane("File")
        file_pane.add_ribbon_widget(RibbonButton(self, self._petugas_action, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self._pelayanan_action, True))

        edit_panel = home_tab.add_ribbon_pane("Edit")
        edit_panel.add_ribbon_widget(RibbonButton(self, self._service1_action, True))
        edit_panel.add_ribbon_widget(RibbonButton(self, self._transaksi_action, True))
        

        """view_panel = home_tab.add_ribbon_pane("View")
        view_panel.add_ribbon_widget(RibbonButton(self, self._zoom_action, True))
        home_tab.add_spacer()"""

        about_tab = self._ribbon.add_ribbon_tab("About")
        info_panel = about_tab.add_ribbon_pane("Info")
        info_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        """info_panel.add_ribbon_widget(RibbonButton(self, self._license_action, True))"""
        info_panel.add_ribbon_widget(RibbonButton(self, self._exit_action, True))

       # -------------      Ribbon Button Functions      -----------------

    def closeEvent(self, close_event):
        pass

    def on_petugas(self):
        petugas_on(self)

    def on_save_to_excel(self):
        pass

    def on_pelayanan(self):
        pelayanan_on(self)   

    def on_service1(self):
        service1_on(self)  

    def on_transaksi(self):
        transaksi_on(self)  

    def on_zoom(self):
        pass

    def on_license(self):
        pass

    def on_about(self):
        text = "APLIKASI CRUD BENGKEL KENDARAAN PosgreSQL"
        text += "Copyright © 2023"
        QMessageBox().about(self, "Tentang Aplikasi", text)

    def app_exit(self):
        sys.exit()