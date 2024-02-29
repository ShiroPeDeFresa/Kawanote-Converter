import sys
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog


class FileTransferApp(QWidget):
    selection_completed = Signal(str, str)  # Señal que emite el nombre del archivo y la carpeta de destino

    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Transfer App")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.file_label = QLabel("Selecciona un archivo (.osu):")
        layout.addWidget(self.file_label)

        self.file_button = QPushButton("Seleccionar archivo")
        self.file_button.clicked.connect(self.select_file)
        layout.addWidget(self.file_button)

        self.dest_label = QLabel("Selecciona una carpeta de destino:")
        layout.addWidget(self.dest_label)

        self.dest_button = QPushButton("Seleccionar destino")
        self.dest_button.clicked.connect(self.select_destination)
        layout.addWidget(self.dest_button)

        self.continue_button = QPushButton("Convertir")
        self.continue_button.clicked.connect(self.continue_process)
        layout.addWidget(self.continue_button)

        self.setLayout(layout)

        # Variables para almacenar los resultados
        self.selected_file = None
        self.selected_destination = None

    def select_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.selected_file = selected_files[0]
                self.file_label.setText(f"Archivo seleccionado: {self.selected_file}")

    def select_destination(self):
        dest_dialog = QFileDialog()
        dest_dialog.setFileMode(QFileDialog.Directory)
        dest_dialog.setOption(QFileDialog.ShowDirsOnly, True)
        if dest_dialog.exec_():
            selected_dir = dest_dialog.selectedFiles()
            if selected_dir:
                self.selected_destination = selected_dir[0]
                self.dest_label.setText(f"Destino seleccionado: {self.selected_destination}")

    def continue_process(self):
        if self.selected_file and self.selected_destination:
            # Emite la señal con los datos seleccionados
            self.selection_completed.emit(self.selected_file, self.selected_destination)
            self.close()
        else:
            print("Debes seleccionar un archivo y una carpeta de destino antes de continuar")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileTransferApp()
    window.show()
    sys.exit(app.exec_())
