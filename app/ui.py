import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class SearchPlusApp(QMainWindow):
    def __init__(self):
        super(SearchPlusApp, self).__init__()
        self.setWindowTitle('SearchPlus')
        self.setGeometry(100, 100, 600, 400)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel('Enter search query:')
        self.input = QLineEdit(self)
        self.button = QPushButton('Search', self)

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SearchPlusApp()
    window.show()
    sys.exit(app.exec())