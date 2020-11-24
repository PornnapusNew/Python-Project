import sys
from PyQt5 import QtWidgets, uic

class Ui (QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('In class 1.ui',self)