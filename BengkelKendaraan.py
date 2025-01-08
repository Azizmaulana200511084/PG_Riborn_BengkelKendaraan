import sys
from PyQt5.QtWidgets import *
from forms.frmLogin import WindowLogin

__author__ = 'umc'

def main():
    a = QApplication(sys.argv)
    a.setQuitOnLastWindowClosed(True)
    login_window = WindowLogin()
    login_window.showFullScreen()
    sys.exit(a.exec_())

main()