from PyQt5 import QtWidgets
import sys
from _radiobuttonForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True)
        self.ui.radioilkokul.setChecked(True)

        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAzerbaycan.toggled.connect(self.onClickedUlke)
        self.ui.radioYunanistan.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)

        self.ui.radioilkokul.toggled.connect(self.onClickedUlke)
        self.ui.radioLise.toggled.connect(self.onClickedUlke)
        self.ui.radioUniversite.toggled.connect(self.onClickedUlke)
        self.ui.radioYuksekLisans.toggled.connect(self.onClickedUlke)

        self.ui.btnUlke.clicked.connect(self.getSelectedUlke)
        self.ui.btnEgitim.clicked.connect(self.getSelectedEgitim)

    def onClickedUlke(self):
        rb = self.sender()

        if rb.isChecked():
            print('Seçilen buton: ' + rb.text())
            
    def onClickedEgitim(self):
        rb = self.sender()

        if rb.isChecked():
            print('Seçilen buton: ' + rb.text())

    def getSelectedUlke(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)
        
        for rb in items:
            if rb.isChecked():
                self.ui.lblUlke.setText('Seçilen ülke: ' + rb.text())

    def getSelectedEgitim(self):
        items = self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton)
        
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText('Seçilen ülke: ' + rb.text())

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()