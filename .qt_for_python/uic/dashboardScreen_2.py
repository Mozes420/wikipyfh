# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'b:\Deep_Learning_Data\vscode_workspace\Jupyter_Notebooks\wikipy\dashboardScreen_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1258, 878)
        Form.setMinimumSize(QtCore.QSize(1258, 878))
        Form.setMaximumSize(QtCore.QSize(1258, 878))
        Form.setBaseSize(QtCore.QSize(1258, 878))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1261, 881))
        self.frame.setStyleSheet("background-color: white")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(560, 90, 681, 150))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Bright\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 1, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 0, 0, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Bright\";")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 1, 1, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 0, 1, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Bright\";")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 1, 2, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout.addWidget(self.textEdit_4, 0, 2, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 250, 1221, 621))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.layoutWidget_2)
        self.widget.setObjectName("widget")
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 0, 871, 621))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.layoutWidget_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.layoutWidget_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2.addWidget(self.frame_5, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 1221, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.textBrowser = QtWidgets.QTextBrowser(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Bright\";")
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox = QtWidgets.QComboBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(700, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setCurrentText("Type your search here ...")
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Bright\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Revisions per User</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">12</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Bright\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Revisions per Day</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">12</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Bright\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Image Count</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">12</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Bright\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt;\">WikiPy</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Results"))
        self.pushButton_2.setText(_translate("Form", "Build Dashboard"))

