import sys
from PyQt5 import QtWidgets
from _dateForm import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.calculate)

    def calculate(self):
        start = self.ui.dateStart.date()
        end = self.ui.dateEnd.date()
        print(start, end)

        print('Days in month: {0}'.format(start.daysInMonth()))
        print('Days in year: {0}'.format(start.daysInYear()))

        print('total days: {0}'.format(start.daysTo(end))) # start ve end arasında kaç gün olduğunu yazdırır.

        now = QDate.currentDate()

        print('total days from now: {0}'.format(start.daysTo(now)))

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())   