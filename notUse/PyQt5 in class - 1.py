import sys
from PyQt5 import QtWidgets, uic

class Ui (QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('In class 1.ui',self)
        self.ok_btn = self.findChild(QtWidgets.QPushButton,'ok_btn') #self.findChildเป็นฟังก์ชันที่ใช้หาargumentใน() ส่วนok_btnคือชื่อ button ที่ตั้งไว้ในPyQt