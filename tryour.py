import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1=QtWidgets.QLabel(w)
    l1.setText('Hello World')
    w.setWindowTitle('PYQt5 lesson 1')
    w.setGeometry(100,100,300,300)
    l1.move(120,140)
    w.show()
    sys.exit(app.exec_())

window()