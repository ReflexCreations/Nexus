from PyQt5.QtWidgets import QApplication
from .component._component_manager import setup_injector
from .main_window import MainWindow

class Application(QApplication):
    def __init__(self):
        super().__init__([])
        injector = setup_injector()
        self.main_window = injector.get(MainWindow)
        self.main_window.show()
        self.exec()