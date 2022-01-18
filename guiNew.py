from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QDesktopWidget


import sys
from random import choice
from gtrends import gtrend

# for gtrends
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# for plotting in qt
#import pyqtgraph as pg
#from pyqtgraph import PlotWidget, plot


class MainWindow(QMainWindow):

    #Initialisieren der Klasse
    def __init__(self):
        super().__init__()

        # Anfangsfenster setzen, Größe auswählen und zentrieren

        self.setWindowTitle("WikiPy")
        screen = QDesktopWidget().screenGeometry()
        self.resize(int(screen.width() / 2), int(screen.height() / 2))
        form = self.geometry()
        x_move_step = (screen.width() - form.width()) / 2
        y_move_step = (screen.height() - form.height()) / 2
        self.move(x_move_step, y_move_step)

        # Einfügen von Text Input Feld

        self.input = QLineEdit("Enter text here")
        self.input.setMaximumHeight(100)
        self.input.setMaximumWidth(200)

        # Einfügen von Button der Anfragen mit Input des Line Edit startet

        self.button = QPushButton("Press Me!")
        self.button.setParent(self)
        self.button.clicked.connect(self.readInput)
        self.button.setMaximumHeight(100)
        self.button.setMaximumWidth(400)

        # Einfügen von Widget in dem der Plot gezeichnet werden soll

        #self.graphWidget = pg.PlotWidget()
        #self.graphWidget.setParent(self)
        

        # Set the central widget of the Window.
        self.setCentralWidget(self.input)
        self.status = self.statusBar()
        self.status.showMessage('Im the status bar', 5000)
        self.center()

    # 
    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


    # Funktion muss in die Klasse

    def gtrend(input):
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(input, cat=0, timeframe='2020-01-01 2022-01-31', geo='US', gprop='')
        keywords = pytrends.suggestions(keyword=input[0])
        df = pd.DataFrame(keywords)
        df.drop(columns= 'mid')
        dfg = pytrends.interest_over_time()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        dfg.plot(ax=ax)
        plt.ylabel('Relative search term frequency')
        plt.xlabel('Date')
        plt.ylim((0,120))
        plt.legend(loc='lower left')
        #plt.plot(dfg, 'k')
        return plt.show()
    


    def readInput(self):  # this function can be used to read user input and call a function based on the input                                                                                   
        print('' + self.input.text())
        text = [self.input.text()]
        gtrend(text)

    #def plotTrend(self):





app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()


""" def gtrendQT(self, input):
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(input, cat=0, timeframe='2020-01-01 2022-01-31', geo='US', gprop='')
        keywords = pytrends.suggestions(keyword=input[0])
        df = pd.DataFrame(keywords)
        df.drop(columns= 'mid')
        dfg = pytrends.interest_over_time()

        self.graphWidget.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget.plot(dfg, pen) """