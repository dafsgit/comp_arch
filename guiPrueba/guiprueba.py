import os
from PyQt5 import QtGui, QtCore
from designer import *

class Ui_MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pb_analize.clicked.connect(self.analize)

    def analize(self):
        fn = self.le_name.text()
        fw = open(f'{fn}.txt', 'w')
        for i in range (0, int(self.le_lnNum.text())):
            fw.write(self.le_text.text() + '\n')
        fw.close()
        
        fr = open(f'{fn}.txt', 'r')
        text = fr.read()
        fr.close()

        vwls = 0
        for ltr in text:
            if ltr in "aeiouAEIOU":
                vwls = vwls + 1
        self.le_vowels.setText(str(vwls))

        cnsnnts = 0
        for ltr in text:
            if ltr in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ":
                cnsnnts = cnsnnts + 1
        self.le_consonants.setText(str(cnsnnts))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.show()
    app.exec_()