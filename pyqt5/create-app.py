import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(200, 200, 500, 500) # soldan ve yukarıdan 200 piksel konum olarak ve 500(en) 500(boy) boyut
    win.setWindowIcon(QIcon('icon.jpg'))
    win.setToolTip('my tooltip')
    
    win.show()
    sys.exit(app.exec_())

window()