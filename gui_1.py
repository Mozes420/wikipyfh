# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wiki_ui_test_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gtrends import gtrend
import crawlerlib
import gtrends

# Klasse = Bestandteile des UI

class Ui_WikiPy(object):
    def setupUi(self, WikiPy):
        WikiPy.setObjectName("WikiPy")
        WikiPy.resize(801, 691)
        self.buttonBox = QtWidgets.QDialogButtonBox(WikiPy)
        self.buttonBox.setGeometry(QtCore.QRect(620, 650, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.widget = QtWidgets.QWidget(WikiPy)
        self.widget.setGeometry(QtCore.QRect(50, 290, 351, 361))
        self.widget.setObjectName("widget")

        self.verticalScrollBar = QtWidgets.QScrollBar(self.widget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(330, -1, 20, 361))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.textEdit = QtWidgets.QTextEdit(WikiPy) # Search bar?
        self.textEdit.setGeometry(QtCore.QRect(50, 40, 231, 31))
        self.textEdit.setObjectName("textEdit")

        self.widget_2 = QtWidgets.QWidget(WikiPy) # Plain Wiki Text
        self.widget_2.setGeometry(QtCore.QRect(50, 80, 351, 191))
        self.widget_2.setObjectName("widget_2")

        self.widget_4 = QtWidgets.QWidget(WikiPy) # Plot 1
        self.widget_4.setGeometry(QtCore.QRect(429, 79, 331, 191))
        self.widget_4.setObjectName("widget_4")
        
        self.widget_3 = QtWidgets.QWidget(WikiPy) # Plot 2
        self.widget_3.setGeometry(QtCore.QRect(430, 290, 331, 201))
        self.widget_3.setObjectName("widget_3")

        self.retranslateUi(WikiPy)

        self.buttonBox.accepted.connect(WikiPy.accept)
        self.buttonBox.rejected.connect(WikiPy.reject)
        QtCore.QMetaObject.connectSlotsByName(WikiPy)

    def retranslateUi(self, WikiPy):
        _translate = QtCore.QCoreApplication.translate
        WikiPy.setWindowTitle(_translate("WikiPy", "Dialog"))
    
    def showplot_gt(self):
        gtrend(['NLP'])


# ausführen

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WikiPy = QtWidgets.QDialog()
    ui = Ui_WikiPy()
    ui.setupUi(WikiPy)
    WikiPy.show()
    sys.exit(app.exec_())

