import json
import sys
import requests
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = uic.loadUi("valute.ui", self)
        self.ui.buttonconvert.clicked.connect(self.converter)
        self.text = ""

    def converter(self):

        from_currency = self.ui.Linevalute.text()
        to_currency = self.ui.Lineconvert.text()
        amount = int(self.ui.Linecash.text())
        url = "http://127.0.0.1:5000/"  # Укажите ваш URL
        response = requests.get(url)
        data = response.json()
        exchange_rate1 = data['rates'][from_currency]
        exchange_rate2 = data['rates'][to_currency]
        if exchange_rate1 > exchange_rate2:
            output_amount = round(((1/exchange_rate1)*amount),2)
            self.ui.Lineget.setText(str(output_amount))
        elif exchange_rate1 < exchange_rate2:
            output_amount = round(((1 * exchange_rate2) * amount), 2)
            self.ui.Lineget.setText(str(output_amount))



if __name__ == '__main__':
    app = QApplication([])
    application = Window()
    application.show()
    sys.exit(app.exec())








