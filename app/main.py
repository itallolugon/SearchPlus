import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QWidget, QPushButton
from ui import Ui_MainWindow
from analyzer import ImageAnalyzer


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.analyzer = ImageAnalyzer()

        self.ui.selectFolderButton.clicked.connect(self.select_folder)
        self.ui.analyzeButton.clicked.connect(self.analyze_images)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.ui.folderPathLabel.setText(folder)

    def analyze_images(self):
        folder_path = self.ui.folderPathLabel.text()
        if folder_path:
            results = self.analyzer.analyze_images_in_folder(folder_path)
            self.ui.resultsLabel.setText('\n'.join(results))
        else:
            self.ui.resultsLabel.setText("Please select a folder first.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
