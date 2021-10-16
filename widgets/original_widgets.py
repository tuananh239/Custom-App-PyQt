from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

class Button(QPushButton):
    def __init__(self, parent = None, icon = None, tool_tip = None, obj_name = None, connect = None):
        super().__init__()
        if parent is not None:
            self.parent = parent
        if obj_name is not None:
            self.setObjectName(obj_name)
        if icon is not None:
            self.setIcon(icon)
        if connect is not None:
            self.clicked.connect(connect)

class Label(QLabel):
    def __init__(self, parent = None, text = None, tool_tip = None, obj_name = None):
        super().__init__()
        if parent is not None:
            self.parent = parent
        if obj_name is not None:
            self.setObjectName(obj_name)
        if text is not None:
            self.setText(text)

class ComboBox(QComboBox):
    def __init__(self, parent = None, icon = None, obj_name = None):
        super().__init__()
        pass

class SpinBox(QSpinBox):
    def __init__(self, scrollWidget=None, *args, **kwargs):
        super(SpinBox, self).__init__(*args, **kwargs)

    def wheelEvent(self, event):
        event.ignore()

class LineEdit(QLineEdit):
    def __init__(self, parent = None, icon = None, tool_tip = None, obj_name = None):
        super().__init__()
        pass

class Action(QAction):
    def __init__(self, parent = None, text = None, icon = None, short_cut = None, tool_tip = None, obj_name = None, connect = None):
        super().__init__()
        if parent is not None:
            self.parent = parent
        if text is not None:
            self.setText(text)
        if short_cut is not None:
            self.setShortcut(short_cut)
        if tool_tip is not None:
            self.setStatusTip(tool_tip)
        if obj_name is not None:
            self.setObjectName(obj_name)
        if connect is not None:
            self.triggered.connect(connect)

class ToolBar(QToolBar):
    def __init__(self, parent = None, text = None):
        super().__init__()
        self.parent = parent
        if text is not None:
            self.setWindowTitle(text)

