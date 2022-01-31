# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'b:\Deep_Learning_Data\vscode_workspace\Jupyter_Notebooks\wikipy\dashboardView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1241, 794)
        Form.setMinimumSize(QtCore.QSize(1231, 781))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1241, 791))
        self.widget.setObjectName("widget")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(860, 190, 341, 541))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(470, 190, 371, 261))
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet("background-color: white")
        self.widget_2.setObjectName("widget_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_3.setGeometry(QtCore.QRect(760, 80, 91, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(1020, 20, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(1114, 20, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_3.setGeometry(QtCore.QRect(700, 130, 201, 41))
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Bright\";")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_4.setGeometry(QtCore.QRect(910, 130, 201, 41))
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Bright\";")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(40, 470, 411, 261))
        self.widget_4.setStyleSheet("background-color: white")
        self.widget_4.setObjectName("widget_4")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(40, 190, 411, 261))
        self.widget_3.setStyleSheet("background-color: white")
        self.widget_3.setObjectName("widget_3")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(470, 470, 371, 261))
        self.widget_5.setAutoFillBackground(False)
        self.widget_5.setStyleSheet("background-color: white")
        self.widget_5.setObjectName("widget_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(490, 130, 201, 41))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Bright\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textEdit_4 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_4.setGeometry(QtCore.QRect(960, 80, 91, 41))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setGeometry(QtCore.QRect(550, 80, 91, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 351, 91))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Bright\";")
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(410, 20, 601, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setCurrentText("Type your search here ...")
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">12</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Results"))
        self.pushButton_2.setText(_translate("Form", "Build Dashboard"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Bright\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Revisions per Day</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Bright\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Image Count</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Bright\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Revisions per User</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">12</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">12</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Bright\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:48pt;\">WikiPy</span></p></body></html>"))

