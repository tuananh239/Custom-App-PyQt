import sys, os
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from app import application


if __name__  == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = application.Application()
    win.show()

    print("App is running!")
    sys.exit(app.exec_())