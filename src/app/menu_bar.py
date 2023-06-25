import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from src.app.logger import Logger
from src.app.widget_registry import Widgets


logger = Logger(__name__, Logger.DEBUG)


class MenuBar(QtWidgets.QMenuBar):
    add_widget = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        file = self.addMenu("&File")
        self.create_file_menu(file)
        widgets = self.addMenu("&Widgets")
        self.create_widgets_menu(widgets)

    def create_file_menu(self, menu: QtWidgets.QMenu):
        menu.addAction("&Open Profile")
        menu.addAction("&Save Profile")

    def create_widgets_menu(self, menu: QtWidgets.QMenu):
        add = menu.addMenu("&Add")
        for key in Widgets.available.keys():
            key_action = add.addAction(f"&{key}")
            def func(_=False, key=key): self.add_widget.emit(key)
            key_action.triggered.connect(func)
