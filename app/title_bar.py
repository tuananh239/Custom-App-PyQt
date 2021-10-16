from PyQt5 import QtWidgets, QtCore, QtGui
from widgets.original_widgets import *
from common.utils import *

class TitleBar(QtWidgets.QFrame):
    def __init__(self, parent):
        super().__init__()

        self.contructor(parent)

        self.elements = struct(
            title = Label(parent=self, text="  Application", obj_name="titleBar"),
            minimize = Button(parent=self, obj_name="minus", connect=self.minimize_window),
            restore = Button(parent=self, obj_name="restore", connect=self.restore_window),
            close =  Button(parent=self, obj_name="close", connect=self.close_window),
        )

        self.init_ui()

    def contructor(self, parent):
        self.parent = parent
        self.setObjectName("titleBar")
        self.setFixedHeight(30)
        self.status = "normal"

    def init_ui(self):
        self.elements.minimize.setMaximumSize(30, 30)
        self.elements.restore.setMaximumSize(30, 30)
        self.elements.close.setMaximumSize(30, 30)

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.elements.title)
        main_layout.addWidget(self.elements.minimize)
        main_layout.addWidget(self.elements.restore)
        main_layout.addWidget(self.elements.close)
    
        self.setLayout(main_layout)

    def close_window(self):
        self.parent.close()

    def minimize_window(self):
        self.parent.showMinimized()

    def restore_window(self):
        if self.status == "normal":
            self.parent.showFullScreen()
            self.status = "max"
        else:
            self.parent.showNormal()
            self.status = "normal"

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton and self.status == "normal":
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.status == "normal":
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.parent.move(self.parent.x() + delta.x(), self.parent.y() + delta.y())
            self.oldPos = event.globalPos()