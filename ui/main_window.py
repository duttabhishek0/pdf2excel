import os
import sys
import pathlib
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from PyQt5.QtGui import QIcon

from pdf_to_excel import conversion


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window properties
        self.setWindowTitle('PDF to Excel Converter')
        self.setWindowIcon(QIcon('resources/app_icon.png'))
        
        # Create widgets
        self.select_file_button = QPushButton('Select PDF File')
        self.select_file_button.clicked.connect(self.select_file)
        
        self.converted_files_list = QListWidget()
        
        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.select_file_button)
        layout.addWidget(self.converted_files_list)
        
        # Create central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Initialize variables
        self.selected_file_path = None
        
    def select_file(self):
        # Show file dialog to select PDF file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select PDF File', '', 'PDF Files (*.pdf)', options=options)
        if file_name:
            self.selected_file_path = pathlib.Path(file_name)
            self.convert_file()
        
    def convert_file(self):
        # Show file dialog to select output Excel file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        output_path, _ = QFileDialog.getSaveFileName
