import sys
import traceback

import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from src.app.logger import Logger
from src.app.main_window import MainWindow
from src.app.widget_registry import Widgets


logger = Logger(__name__, Logger.DEBUG)


class Application(QtWidgets.QApplication):
    def __init__(self):
        super().__init__()
        sys.excepthook = self._excepthook

        self.widgets = Widgets()
        self.main_window = MainWindow()
        self.main_window.menu_bar.add_widget.connect(self.add_widget)

    def _excepthook(self, exc_type, exc_val, exc_tb):
        msg = "Uncaught exception during application start-up - \n"
        tb = "".join(traceback.format_exception(exc_type, exc_val, exc_tb))
        logger.critical(msg + tb)

    def run(self):
        logger.debug("Application initialised.")
        self.main_window.show()
        return self.exec()

    @QtCore.Slot(str)
    def add_widget(self, key):
        widget = self.widgets.get_widget(key)
        if not widget:
            logger.warning(f"Couldn't load widget {key=}")
            return
        self.main_window.load_view(widget)
