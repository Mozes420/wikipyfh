# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'b:\Deep_Learning_Data\vscode_workspace\Jupyter_Notebooks\wikipy\welcomeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(1185, 807)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1080, 720))
        Dialog.setSizeGripEnabled(True)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1251, 831))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(1231, 781))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 245, 228, 255), stop:1 rgba(255, 255, 255, 255));")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(690, 420, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(290, 230, 521, 91))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Bright\";")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 420, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(200, 420, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Lucida Bright\";")
        self.comboBox.setEditable(True)
        self.comboBox.setCurrentText("Type your search here ...")
        self.comboBox.setMaxVisibleItems(7)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WikiPy"))
        self.pushButton.setText(_translate("Dialog", "Results"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Bright\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:48pt;\">WikiPy</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Go!"))

