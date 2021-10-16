import sys, os
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from app import main_window, title_bar
from widgets.original_widgets import *
from common.utils import *
from widgets.custom_widgets import *
from resources.themes import original

class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Application, self).__init__()

        self.modules = struct(
            title_bar = title_bar.TitleBar(self),
            main_window = main_window.MainWindow()
        )

        self.init_ui()
        self.contructor()

    def contructor(self):
        self._gripSize = 5

        self.sideGrips = [
            SideGrip(self, QtCore.Qt.LeftEdge),
            SideGrip(self, QtCore.Qt.TopEdge),
            SideGrip(self, QtCore.Qt.RightEdge),
            SideGrip(self, QtCore.Qt.BottomEdge)
        ]

        self.cornerGrips = [QtWidgets.QSizeGrip(self) for i in range(4)]

    def init_ui(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.resize(1366, 768)
        self.setStyleSheet(original.styleSheet)
        
        self.mainWidget = QtWidgets.QWidget()

        main_layout = QtWidgets.QVBoxLayout(self.mainWidget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.modules.title_bar)
        main_layout.addWidget(self.modules.main_window)

        self.mainWidget.setLayout(main_layout)
        self.setCentralWidget(self.mainWidget)

    
    @property
    def gripSize(self):
        return self._gripSize

    def setGripSize(self, size):
        if size == self._gripSize:
            return
        self._gripSize = max(2, size)
        self.updateGrips()

    def updateGrips(self):
        self.setContentsMargins(0, 0, 0, 0)
        outRect = self.rect()
        inRect = outRect.adjusted(self.gripSize, self.gripSize, -self.gripSize, -self.gripSize)

        self.cornerGrips[0].setGeometry(QtCore.QRect(outRect.topLeft(), inRect.topLeft()))
        self.cornerGrips[1].setGeometry(QtCore.QRect(outRect.topRight(), inRect.topRight()).normalized())
        self.cornerGrips[2].setGeometry(QtCore.QRect(outRect.bottomRight(), inRect.bottomRight()))
        self.cornerGrips[3].setGeometry(QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()))

        self.sideGrips[0].setGeometry(0, inRect.top(), self.gripSize, inRect.height())
        self.sideGrips[1].setGeometry(inRect.left(), 0, inRect.width(), self.gripSize)
        self.sideGrips[2].setGeometry(inRect.left() + inRect.width(), inRect.top(), self.gripSize, inRect.height())
        self.sideGrips[3].setGeometry(self.gripSize, inRect.top() + inRect.height(), inRect.width(), self.gripSize)

    def resizeEvent(self, event):
        QtWidgets.QMainWindow.resizeEvent(self, event)
        self.updateGrips()