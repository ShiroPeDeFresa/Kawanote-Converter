import sys
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog

import Interface



def handle_selection(file, destination):
    print("Archivo seleccionado:", file)
    print("Destino seleccionado:", destination)

app = QApplication(sys.argv)
window = Interface.FileTransferApp()

window.selection_completed.connect(handle_selection)  # Conexión a la señal

window.show()
sys.exit(app.exec_())