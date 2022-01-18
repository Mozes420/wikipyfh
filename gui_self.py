### PyQt5 GUI for WikiPy App ###

### Imports ###

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import crawlerlib
from gtrends import gtrend
import sys

### Plot Klasse? ###

class GTrendCanvas(FigureCanvasQTAgg):

    def __init__(self):
        fig = gtrend(['NLP'])
        super(GTrendCanvas, self).__init__(fig)

### GUI Klasse ###

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        gt = GTrendCanvas()
        self.setCentralWidget(gt)
        self.show()



app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()