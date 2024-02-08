#Schrauber Steuerung auf Microcontroller Basis
#Technikerarbeit Julika Haubner 2024
#Firma Hansgrohe SE - Berufliche Schulen Oberndorf-Sulz

import sys

from PySide6.QtWidgets import QApplication

from setting_window import SettingWindow
from main_window import MainWindow

from cvir import CVIR
from toolbox import Toolbox
from product import Product

if __name__ == "__main__":
    toolbox = Toolbox()
    product = Product()
    cvir = CVIR()

    # Start Application
    app = QApplication(sys.argv)
    # Initialize SettingWindow
    setting_window = SettingWindow(product)
    # Start MainWindow
    window = MainWindow(setting_window, product, toolbox, cvir)
    window.showFullScreen()

    # Execute Application
    sys.exit(app.exec())
