# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 351)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("GUI_prueba")
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.le_name = QtWidgets.QLineEdit(self.centralwidget)
        self.le_name.setGeometry(QtCore.QRect(20, 30, 141, 21))
        self.le_name.setObjectName("le_name")
        self.le_text = QtWidgets.QLineEdit(self.centralwidget)
        self.le_text.setGeometry(QtCore.QRect(20, 80, 141, 51))
        self.le_text.setObjectName("le_text")
        self.le_lnNum = QtWidgets.QLineEdit(self.centralwidget)
        self.le_lnNum.setGeometry(QtCore.QRect(20, 160, 141, 21))
        self.le_lnNum.setObjectName("le_lnNum")
        self.lbl_name = QtWidgets.QLabel(self.centralwidget)
        self.lbl_name.setGeometry(QtCore.QRect(200, 32, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name.setFont(font)
        self.lbl_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_name.setWordWrap(False)
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_text = QtWidgets.QLabel(self.centralwidget)
        self.lbl_text.setGeometry(QtCore.QRect(200, 80, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_text.setFont(font)
        self.lbl_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_text.setWordWrap(False)
        self.lbl_text.setObjectName("lbl_text")
        self.lbl_lnNum = QtWidgets.QLabel(self.centralwidget)
        self.lbl_lnNum.setGeometry(QtCore.QRect(200, 160, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_lnNum.setFont(font)
        self.lbl_lnNum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_lnNum.setWordWrap(False)
        self.lbl_lnNum.setObjectName("lbl_lnNum")
        self.lbl_vowels = QtWidgets.QLabel(self.centralwidget)
        self.lbl_vowels.setGeometry(QtCore.QRect(40, 250, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_vowels.setFont(font)
        self.lbl_vowels.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_vowels.setWordWrap(False)
        self.lbl_vowels.setObjectName("lbl_vowels")
        self.lbl_consonants = QtWidgets.QLabel(self.centralwidget)
        self.lbl_consonants.setGeometry(QtCore.QRect(220, 250, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_consonants.setFont(font)
        self.lbl_consonants.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_consonants.setWordWrap(False)
        self.lbl_consonants.setObjectName("lbl_consonants")
        self.pb_analize = QtWidgets.QPushButton(self.centralwidget)
        self.pb_analize.setGeometry(QtCore.QRect(160, 200, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_analize.setFont(font)
        self.pb_analize.setObjectName("pb_analize")
        self.le_vowels = QtWidgets.QLineEdit(self.centralwidget)
        self.le_vowels.setGeometry(QtCore.QRect(80, 280, 61, 21))
        self.le_vowels.setObjectName("le_vowels")
        self.le_consonants = QtWidgets.QLineEdit(self.centralwidget)
        self.le_consonants.setGeometry(QtCore.QRect(260, 280, 61, 21))
        self.le_consonants.setObjectName("le_consonants")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_name.setText(_translate("MainWindow", "Nombre del arhivo"))
        self.lbl_text.setText(_translate("MainWindow", "Texto a escribir"))
        self.lbl_lnNum.setText(_translate("MainWindow", "Número de líneas en archivo"))
        self.lbl_vowels.setText(_translate("MainWindow", "Número de vocales"))
        self.lbl_consonants.setText(_translate("MainWindow", "Número de consonantes"))
        self.pb_analize.setText(_translate("MainWindow", "Analizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())