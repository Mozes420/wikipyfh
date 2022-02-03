from webbrowser import get
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QApplication,
    QLabel,
    QPushButton,
    QLineEdit,
    QDesktopWidget,
    QGridLayout,
    QGroupBox,
    QTextEdit,
    QComboBox,
    QHBoxLayout,
    QFormLayout,
    QVBoxLayout,
    QTextBrowser,
    QGraphicsView
)
import PyQt5.QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from dropdownList import getDropdownList
from PyQt5 import uic
import sys
import random
from random import choice
from crawlerlib import getSoup
#from gtrends import gtrend
import numpy as np
from PyQt5 import QtGui
# for gtrends
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# for plotting in qt
#import pyqtgraph as pg
#from pyqtgraph import PlotWidget, plot

# for crawlerlib
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import re
import urllib
from gtrends import gtrend

from vis1 import getBlankText, getURL
import wikipedia
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


# Einstiegsbildschirm

class WelcomeScreen(QtWidgets.QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        uic.loadUi('welcomeScreen.ui', self)

        self.checkerWelcome = False

        self.testBox = GroupBox()

        #Festlegen von Params 
        self.setWindowTitle("kWiki")
        self.resize(800,600)

        #Finden der UI-Widgets
        self.logo = self.findChild(QLabel, 'label')
        image_path = 'kwiki.JPG'
        image_profile = QtGui.QImage(image_path)
        image_profile = image_profile.scaled(250,250, aspectRatioMode = PyQt5.QtCore.Qt.KeepAspectRatio, transformMode = PyQt5.QtCore.Qt.SmoothTransformation)
        self.logo.setPixmap(QtGui.QPixmap.fromImage(image_profile))
        self.inputQuery = self.findChild(QComboBox, 'comboBox')
        self.buttonOne = self.findChild(QPushButton, 'pushButton')
        self.buttonOne.clicked.connect(self.setDropdownItems)
        self.buttonTwo = self.findChild(QPushButton, 'pushButton_2')
        self.buttonTwo.clicked.connect(self.call)

        # Dropdown Items einfügen
    def setDropdownItems(self):
        print("searching results for: " + self.inputQuery.currentText())
        list = getDropdownList(self.inputQuery.currentText())
        self.inputQuery.addItems(list)
        self.checkerWelcome = True
        print("done")
        
        # TEST Index setzen zweite Seite
    def setIndexToOne(self):
        print('set index to one function call')
        WikiPy.setCurrentIndex(1)
        self.callFunctions()
        
        # Funktionen aufrufen -> über Child Klasse
    def callFunctions(self):
        #WikiPy.setCurrentIndex(0)
        print(self.inputQuery.currentText())
        inp = self.inputQuery.currentText()
        text = getBlankText(inp)[0]
        #WikiPy.setCurrentIndex(1)
        self.testBox.callFunctions(text, inp)



    def call(self):
        if(self.checkerWelcome):
            #self.buttonTwo.clicked.connect(self.setIndexToOne)
            print("creating...")
            self.setIndexToOne()
        else: print("You need to get search results first!")



# Dashboard Bildschirm

class GroupBox(QtWidgets.QWidget):

    #Initialisieren der Klasse
    def __init__(self):
        super().__init__()

        # Anfangsfenster setzen, Größe auswählen und zentrieren

        self.checker = False

        # self.setStyleSheet('''
        #     QWidget {
        #         background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(217, 224, 255, 255), stop:1 rgba(255, 255, 255, 255));
        #         }
        #     ''')
    
        self.layout = QHBoxLayout(self)
        self.groupbox = QGroupBox("Start you Knowledge!", checkable=False)
        self.layout.addWidget(self.groupbox)

        # Einfügen von Text Input Feld

        self.input = QLineEdit("Type your search ...")
        self.input.setMaximumHeight(100)
        self.input.setMaximumWidth(400)

        # Einfügen von Button der Anfragen mit Input des Line Edit startet
        ##########################################################
        self.button = QPushButton("Get Search Results")
        self.button.setParent(self)
        #self.button.clicked.connect(self.readInput)
        self.button.clicked.connect(self.setDropdownItems)
        self.button.setMaximumHeight(25)
        self.button.setMaximumWidth(200)

        self.comboBox = QComboBox(self)
        self.comboBox.setEditable(True)
        self.comboBox.setMinimumWidth(300)

        self.button2 = QPushButton("Go!")
        self.button2.setParent(self)
        #self.button2.clicked.connect(self.readInput)
        self.button2.setMaximumHeight(25)
        self.button2.setMaximumWidth(200)
        self.button2.clicked.connect(self.call)

        # Einfügen von KPI Boxen
        #############################################################
        self.revsPerDayText = QTextBrowser()
        self.revsPerDayText.setText('Revisions per Day')
        self.revsPerUserText = QTextBrowser()
        self.revsPerUserText.setText('Revisions per User')
        self.imgCountText = QTextBrowser()
        self.imgCountText.setText('Image Count')

        self.revsPerDayKPI = QTextBrowser()
        self.revsPerDayKPI.setText('0')
        self.revsPerUserKPI = QTextBrowser()
        self.revsPerUserKPI.setText('0')
        self.imgCountKPI = QTextBrowser()
        self.imgCountKPI.setText('0')


        # Einfügen von befüllten Widgets
        #####################################################
        self.canvasTrend = FigureCanvas(Figure())
        self.canvasTrend.setParent(self)
        self.canvasTrend.setFixedWidth(400)
        self.canvasTrend.setFixedHeight(200)

        self.canvasCloud = FigureCanvas(Figure())
        self.canvasCloud.setParent(self)
        self.canvasCloud.setFixedWidth(400)
        self.canvasCloud.setFixedHeight(250)

        self.canvasRevs = FigureCanvas(Figure())
        self.canvasRevs.setParent(self)
        self.canvasRevs.setFixedWidth(400)
        self.canvasRevs.setFixedHeight(250)

        self.canvasImg = FigureCanvas(Figure())
        self.canvasImg.setParent(self)
        self.canvasImg.setFixedWidth(400)
        self.canvasImg.setFixedHeight(250)

        self.blankText = QTextEdit(self) 
        self.blankText.setMinimumWidth(400)
        self.blankText.setMinimumHeight(500)
        self.blankText.setParent(self)


        # Erstellen des Layouts
        #############################################################
        self.outerLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.grid = QGridLayout()
        self.textLayout = QHBoxLayout()
        self.kpiLayout = QHBoxLayout()
        self.kpiTextLayout = QHBoxLayout()

        self.groupbox.setLayout(self.outerLayout)
        #self.grid.addWidget(self.input, 0,0,1,3, PyQt5.QtCore.Qt.AlignCenter)
        self.outerLayout.addLayout(self.topLayout)
        self.outerLayout.addLayout(self.kpiTextLayout)
        self.outerLayout.addLayout(self.kpiLayout)
        self.outerLayout.addLayout(self.textLayout)
        self.textLayout.addLayout(self.grid)

        self.topLayout.addWidget(self.comboBox)
        self.topLayout.addWidget(self.button)
        self.topLayout.addWidget(self.button2)

        self.kpiTextLayout.addWidget(self.revsPerDayKPI)
        self.kpiTextLayout.addWidget(self.revsPerUserKPI)
        self.kpiTextLayout.addWidget(self.imgCountKPI)

        self.kpiLayout.addWidget(self.revsPerDayText)
        self.kpiLayout.addWidget(self.revsPerUserText)
        self.kpiLayout.addWidget(self.imgCountText)

        self.textLayout.addWidget(self.blankText, PyQt5.QtCore.Qt.AlignTop)

        self.grid.addWidget(self.canvasTrend, 0,0)
        self.grid.addWidget(self.canvasCloud, 0,1)
        self.grid.addWidget(self.canvasRevs, 1,0)
        self.grid.addWidget(self.canvasImg,1,1)

        #self.grid.addWidget(self.blankText, 1,2, PyQt5.QtCore.Qt.AlignCenter)


    ############# FUNKTIONEN ##############################
    # Funktion aufrufen Welcome Screen

    def start(self):
        welcomeScreen = WelcomeScreen()
        if welcomeScreen.exec_():
            self.show()
        else:
            welcomeScreen.exec_()

    # Funktion muss in die Klasse

    def setDropdownItems(self):
        print("searching results for: " + self.comboBox.currentText())
        list = getDropdownList(self.comboBox.currentText())
        self.comboBox.addItems(list)
        self.button2.clicked.connect(self.callFunctions)
        self.checker = True
        print("done")


    # def gtrend(self, input):
    #      pytrends = TrendReq(hl='en-US', tz=360)
    #      pytrends.build_payload(input, cat=0, timeframe='2020-01-01 2022-01-31', geo='US', gprop='')
    #      keywords = pytrends.suggestions(keyword=input[0])
    #      df = pd.DataFrame(keywords)
    #      df.drop(columns= 'mid')
    #      dfg = pytrends.interest_over_time().drop(labels=['isPartial'],axis='columns')
    #      self.canvasTrend = FigureCanvas(Figure())
    #      self.canvasTrend.axes = self.canvasTrend.figure.add_subplot(111)
    #      self.canvasTrend.axes.clear()
    #      self.canvasTrend.axes.set_title('Relative Search Term Frequency')
    #      self.canvasTrend.axes.plot(dfg)
    #      self.canvasTrend.axes.legend((dfg[0:0]),loc='upper right')
    #      self.canvasTrend.draw()
    #      self.canvasTrend.axes.set_xlabel('Time')
    #      self.canvasTrend.axes.set_ylabel('Frequency')
    #      self.canvasTrend.axes.set_xticklabels(labels=dfg.index[:,], rotation=45)
    #      self.canvasTrend.setMaximumWidth(400)
    #      self.canvasTrend.setMaximumHeight(300)
    #      self.grid.addWidget(self.canvasTrend, 1,0, PyQt5.QtCore.Qt.AlignCenter)
    

    def drawWordCloud(self, text):
         stopwords = set(STOPWORDS)
         stopwords.update(["e.g"])
         wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(text)
         self.canvasCloud = FigureCanvas(Figure())
         self.axes = self.canvasCloud.figure.add_subplot()
         self.axes.axis('off')
         self.axes.imshow(wordcloud)
         self.canvasCloud.setMaximumWidth(400)
         self.canvasCloud.setMaximumHeight(300)
         self.grid.addWidget(self.canvasCloud, 1,1, PyQt5.QtCore.Qt.AlignCenter)


    def writeTextWiki(self, text):
         self.blankText.setText(text)
         print('writetextwiki')
         self.grid.addWidget(self.blankText, 1,2, PyQt5.QtCore.Qt.AlignCenter)
        

    def callFunctions(self, text, inp):
        inp = self.comboBox.currentText()
        #self.gtrend([inp])
        self.drawWordCloud(text)
        self.writeTextWiki(text)

    def call(self):
        if(self.checker):
            self.button2.clicked.connect(self.callFunctions)
            print("creating...")
        else: print("You need to get search results first!")
        


####################### MAIN #####################################


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    WikiPy = QtWidgets.QStackedWidget()
    welcomescreen = WelcomeScreen()
    #groupbox = GroupBox()
    WikiPy.addWidget(welcomescreen)
    WikiPy.addWidget(welcomescreen.testBox)
    print(WikiPy.currentIndex())
    WikiPy.show()

    sys.exit(app.exec_())