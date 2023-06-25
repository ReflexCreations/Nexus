import PySide6.QtWidgets as QtWidgets


class LogViewer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.setReadOnly(True)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.text_edit)

    def update_log(self, message):
        self.text_edit.append(message)
