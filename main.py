# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import NueralNet as NN
    
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.Category = QtWidgets.QLabel("Draw: Moon")
        self.button = QtWidgets.QPushButton("Test")
        self.output = None
        self.toolBar = self.addToolBar("toolbar")
        self.toolBar.addWidget(self.Category)
        self.toolBar.addWidget(self.button)
        self.CANVAS = Canvas()
        self.setCentralWidget(self.CANVAS)
        self.button.clicked.connect(self.buttonClicked)
        
    def buttonClicked(self):
        self.CANVAS.canvas.save("test.png")
        model = NN.CNN("sketches_png/Categories/Space/Images")
        model.load("sketches_png/Categories/Space/saved_model.pb")
        category = model("test.png")
        self.output = QtWidgets.QLabel(category)
        self.toolBar.addWidget(self.output)

class Canvas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.canvas = QtGui.QPixmap(900, 900)
        self.canvas.fill(Qt.white)
        self.points = None
    
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        Origin = QtCore.QPoint(0,0)
        painter.drawPixmap(Origin, self.canvas)
        
    def mousePressEvent(self, event):
        pen = QtGui.QPen()
        painter = QtGui.QPainter(self.canvas)
        pen.setWidth(3)
        painter.setPen(pen)
        pen.setColor(Qt.black)
        
        self.points = event.pos()
        painter.drawPoint(self.points)
        self.update()
    def mouseMoveEvent(self, event):
        pen = QtGui.QPen()
        painter = QtGui.QPainter(self.canvas)
        pen.setWidth(3)
        painter.setPen(pen)
        pen.setColor(Qt.black)
        
        painter.drawLine(self.points, event.pos())
        self.update()
        self.points = event.pos()
    def sizeHint(self):
        return self.canvas.size()
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
