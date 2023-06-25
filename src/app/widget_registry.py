import importlib
import pathlib

import PySide6.QtWidgets as QtWidgets


class Widgets:
    available = {}
    active = {}

    def __init__(self):
        parent_dir = pathlib.Path(__file__).parent.parent
        widgets_dir = parent_dir / "widgets"
        for file in widgets_dir.glob("*.py"):
            module_name = f'{parent_dir.name}.{widgets_dir.name}.{file.stem}'
            module = importlib.import_module(module_name)
            for name in dir(module):
                member = getattr(module, name)
                if isinstance(member, type):
                    if issubclass(member, QtWidgets.QWidget):
                        self.available[name] = member

    def get_widget(self, widget_name):
        for key, cls in self.available.items():
            if key == widget_name:
                self.available.pop(key)
                inst = cls()
                self.active[key] = inst
                return inst
