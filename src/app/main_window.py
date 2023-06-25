import PySide6.QtWidgets as QtWidgets

from src.app.menu_bar import MenuBar


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("RE:Flex Nexus")
        self.setMinimumSize(800, 600)
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def load_view(self, view):
        self.layout.addWidget(view)

    def _load_stylesheet(self):
        with open("stylesheet.qss", "r") as f:
            return f.read()
