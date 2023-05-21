from ..helper import inject, slot
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class Model:
    def __init__(self):
        self.log_messages = []

    def add_message(self, message):
        self.log_messages.append(message)

class View(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)

    def update_log(self, message):
        self.text_edit.append(message)

class Controller:
    @inject
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    @slot
    def update(self, message):
        self.model.add_message(message)
        self.view.update_log(message)