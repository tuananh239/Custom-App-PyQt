from PyQt5 import QtWidgets, QtCore, QtGui
from common.utils import *
from widgets.original_widgets import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.contructor()

        self.actions = struct(
            new = Action(text = "New...", short_cut = "Ctrl+N"),
            open = Action(text = "Open...", short_cut = "Ctrl + O")
        )

        self.menu = struct(
            file = new_menu(
                menu_bar = self.menuBar(),
                text = "&File",
                args = [
                    self.actions.new,
                    self.actions.open
                ]
            )
        )

        self.init_ui()

    def contructor(self):
        self.setObjectName("content")
        self.setMaximumHeight(160000)

    def init_ui(self):
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)