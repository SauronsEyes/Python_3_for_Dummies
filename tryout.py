import sys
from PyQt5 import QtWidgets,QtGui
#Importing required Libraries


#Defining function window Which creates Window
def window():
    app = QtWidgets.QApplication(sys.argv)
    mPlatform = QtWidgets.QWidget()
    background = QtWidgets.QLabel(mPlatform)
    clickMe = QtWidgets.QPushButton(mPlatform)
    headText = QtWidgets.QLabel(mPlatform)
    background.setPixmap(QtGui.QPixmap('world.png'))
    
    v_box = QtWidgets.QVBoxLayout()
    h_box=QtWidgets.QHBoxLayout()
    
    clickMe.setText("Like us")
    headText.setText('Hello World')
    
    h_box.addStretch()
    h_box.addWidget(headText)
    h_box.addStretch()
    
    v_box.addWidget(background)
    v_box.addLayout(h_box)
    v_box.addWidget(clickMe)
    mPlatform.setLayout(v_box)
    
    mPlatform.setWindowTitle('Our World')
    mPlatform.setGeometry(30,30,300,300)

    mPlatform.show()
    sys.exit(app.exec_())

window()