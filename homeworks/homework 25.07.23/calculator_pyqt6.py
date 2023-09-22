from PyQt6 import QtWidgets, QtCore, QtGui, uic
import sys
import math as mt;
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = uic.loadUi("calc.ui", self)
        self.ui.button1.clicked.connect(lambda: self.NumBut(1))
        self.ui.button2.clicked.connect(lambda: self.NumBut(2))
        self.ui.button3.clicked.connect(lambda: self.NumBut(3))
        self.ui.button4.clicked.connect(lambda: self.NumBut(4))
        self.ui.button5.clicked.connect(lambda: self.NumBut(5))
        self.ui.button6.clicked.connect(lambda: self.NumBut(6))
        self.ui.button7.clicked.connect(lambda: self.NumBut(7))
        self.ui.button8.clicked.connect(lambda: self.NumBut(8))
        self.ui.button9.clicked.connect(lambda: self.NumBut(9))
        self.ui.button_0.clicked.connect(lambda: self.NumBut(0))

        self.ui.button_pluss.clicked.connect(lambda: self.NumBut('+'))
        self.ui.button_minuss.clicked.connect(lambda: self.NumBut('-'))
        self.ui.button_dividee.clicked.connect(lambda: self.NumBut('/'))
        self.ui.button_multiplyy.clicked.connect(lambda: self.NumBut('*'))


        self.ui.button_deletee.clicked.connect(self.Clear)

        self.ui.button_equal.clicked.connect(self.Equal)
    def Clear(self):
        self.ui.label.clear()

    def Equal(self):
        min = '-'
        plus = '+'
        Split = '/'
        multiply = '*'
        compare = self.ui.label.text()
        if '-' in compare:
            a = compare.split('-')
            n = float(a[0])
            nl = float(a[1])
            f = float(n - nl)
            self.ui.label.setText(str(mt.floor(f)))
        elif plus in compare:
            a = compare.split('+')
            n = float(a[0])
            nl = float(a[1])
            f = float(n + nl)
            self.ui.label.setText(str(mt.floor(f)))
        elif Split in compare:
            a = compare.split('/')
            n = float(a[0])
            nl = float(a[1])
            f = float(n / nl)
            self.ui.label.setText(str(mt.floor(f)))
        elif multiply in compare:
            a = compare.split('*')
            n = float(a[0])
            nl = float(a[1])
            f = float(n * nl)
            self.ui.label.setText(str(mt.floor(f)))
        self.ui.label.setText(self.ui.label.text())

    def NumBut(self,num):
        n = str(num)
        self.ui.label.setText(self.ui.label.text()+n)
app = QtWidgets.QApplication([])
window = Window()
window.show()
app.exec()
