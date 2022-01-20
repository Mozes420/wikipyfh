from webbrowser import get
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QDesktopWidget, QGridLayout, QGroupBox, QTextEdit, QComboBox
import PyQt5.QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from dropdownList import getDropdownList

import sys
import random
from random import choice
from crawlerlib import getSoup
#from gtrends import gtrend
import numpy as np

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


class GroupBox(QtWidgets.QWidget):

    #Initialisieren der Klasse
    def __init__(self):
        super().__init__()

        # Anfangsfenster setzen, Größe auswählen und zentrieren

        self.checker = False

        self.setWindowTitle("WikiPy")
        screen = QDesktopWidget().screenGeometry()
        self.resize(int(screen.width()/2), int(screen.height()/2))
        form = self.geometry()
        x_move_step = (screen.width() - form.width())
        y_move_step = (screen.height() - form.height())
        self.move(int(x_move_step/2), int(y_move_step/2))
    
        self.layout = QGridLayout(self)
        self.groupbox = QGroupBox("Start you Knowledge!", checkable=False)
        self.layout.addWidget(self.groupbox)

        # Einfügen von Text Input Feld

        self.input = QLineEdit("Type your search ...")
        self.input.setMaximumHeight(100)
        self.input.setMaximumWidth(400)

        # Einfügen von Button der Anfragen mit Input des Line Edit startet

        self.button = QPushButton("Go!")
        self.button.setParent(self)
        #self.button.clicked.connect(self.readInput)
        self.button.clicked.connect(self.setDropdownItems)
        self.button.setMaximumHeight(50)
        self.button.setMaximumWidth(200)


        
        self.comboBox = QComboBox(self)
        self.comboBox.setEditable(True)
        self.comboBox.setMinimumWidth(300)
        #self.comboBox.currentIndexChanged.connect(self.setDropdownItems)
        #self.comboBox.currentIndexChanged.connect(self.callFunctions("test"))


        self.button2 = QPushButton("Go!")
        self.button2.setParent(self)
        #self.button2.clicked.connect(self.readInput)
        self.button2.setMaximumHeight(50)
        self.button2.setMaximumWidth(200)
        self.button2.clicked.connect(self.call)
            


        

        # Einfügen von befüllten Widgets
        #############################################
        self.canvasTrend = FigureCanvas(Figure())
        self.canvasTrend.setParent(self)
        self.canvasTrend.setMaximumWidth(400)
        self.canvasTrend.setMaximumHeight(300)

        self.canvasCloud = FigureCanvas(Figure())
        self.canvasCloud.setParent(self)
        self.canvasCloud.setMaximumWidth(400)
        self.canvasCloud.setMaximumHeight(300)

        self.blankText = QTextEdit(self) ################ WORK IN PROGRESS
        self.blankText.setMinimumWidth(300)
        self.blankText.setMinimumHeight(400)
        self.blankText.setParent(self)

        self.grid = QGridLayout()
        self.groupbox.setLayout(self.grid)
        #self.grid.addWidget(self.input, 0,0,1,3, PyQt5.QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.button, 0,1,1,2, PyQt5.QtCore.Qt.AlignRight)
        self.grid.addWidget(self.button2, 0,1,1,2, PyQt5.QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.canvasTrend, 1,0, PyQt5.QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.canvasCloud, 1,1, PyQt5.QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.blankText, 1,2, PyQt5.QtCore.Qt.AlignCenter) ####################### WIP
        self.grid.addWidget(self.comboBox, 0,0,1,3, PyQt5.QtCore.Qt.AlignCenter)


    # Funktion muss in die Klasse

    def gtrend(self, input):
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(input, cat=0, timeframe='2020-01-01 2022-01-31', geo='US', gprop='')
        keywords = pytrends.suggestions(keyword=input[0])
        df = pd.DataFrame(keywords)
        df.drop(columns= 'mid')
        dfg = pytrends.interest_over_time().drop(labels=['isPartial'],axis='columns')
        self.canvasTrend = FigureCanvas(Figure())
        self.canvasTrend.axes = self.canvasTrend.figure.add_subplot(111)
        self.canvasTrend.axes.clear()
        self.canvasTrend.axes.set_title('Relative Search Term Frequency')
        self.canvasTrend.axes.plot(dfg)
        self.canvasTrend.axes.legend((dfg[0:0]),loc='upper right')
        self.canvasTrend.draw()
        self.canvasTrend.axes.set_xlabel('Time')
        self.canvasTrend.axes.set_ylabel('Frequency')
        self.canvasTrend.axes.set_xticklabels(labels=dfg.index[:,], rotation=45)
        self.canvasTrend.setMaximumWidth(400)
        self.canvasTrend.setMaximumHeight(300)
        self.grid.addWidget(self.canvasTrend, 1,0, PyQt5.QtCore.Qt.AlignCenter)
    

    def drawWordCloud(self, keyword):
        text = getBlankText(keyword)[0]
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


    def writeTextWiki(self, keyword): ########################### WIP 
         text = getBlankText(keyword)[0]
         self.blankText.setText(text)
         self.grid.addWidget(self.blankText, 1,2, PyQt5.QtCore.Qt.AlignCenter)


    def readInput(self):  # this function can be used to read user input and call a function based on the input                                                                                   
        print('' + self.input.text())
        text = [self.input.text()]
        self.gtrend(text)
        self.drawWordCloud(self.input.text())
        self.writeTextWiki(self.input.text()) ################# WIP

    def setDropdownItems(self):
        list = getDropdownList(self.comboBox.currentText())
        self.comboBox.addItems(list)
        self.checker = True

    def callFunctions(self):
        self.gtrend([self.comboBox.currentText()])
        self.drawWordCloud(self.comboBox.currentText())
        self.writeTextWiki(self.comboBox.currentText())

    def call(self):
        if(self.checker):
            self.button2.clicked.connect(self.callFunctions)
            print("called call")





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    WikiPy = GroupBox()
    WikiPy.show()
    sys.exit(app.exec_())