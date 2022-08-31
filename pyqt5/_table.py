from math import prod
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys
from _tableForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.btnSave.clicked.connect(self.saveProduct)
        self.ui.tableProducts.doubleClicked.connect(self.doubleClick)

    def doubleClick(self):
        for item in self.ui.tableProducts.selectedItems():
            print(item.row(), item.column(), item.text())

    def saveProduct(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()

        if name and price is not None:
            rowCount = self.ui.tableProducts.rowCount()
            print(rowCount)
            self.ui.tableProducts.insertRow(rowCount)
            self.ui.tableProducts.setItem(rowCount, 0, QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount, 1, QTableWidgetItem(price))

    def loadProducts(self):

        products = [
            {'name': 'Samsung S5', 'price': 2000},
            {'name': 'Samsung S6', 'price': 3000},
            {'name': 'Samsung S7', 'price': 4000},
            {'name': 'Samsung S8', 'price': 5000},
        ]

        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        self.ui.tableProducts.setHorizontalHeaderLabels(('Name', 'Price'))
        self.ui.tableProducts.setColumnWidth(0, 100) # 0. kolon 120 genişliğinde
        self.ui.tableProducts.setColumnWidth(1, 50)

        rowIndex = 0
        for product in products:
            self.ui.tableProducts.setItem(rowIndex, 0, QTableWidgetItem(product['name'])) # 0. satırın 0. kolonuna item ekleme
            self.ui.tableProducts.setItem(rowIndex, 1, QTableWidgetItem(str(product['price']))) # 0. satırın 1. kolonuna item ekleme
            rowIndex += 1
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()