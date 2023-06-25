import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from src.app.logger import Logger


logger = Logger(__name__)


class PadInterface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.connect_button = QtWidgets.QPushButton("Connect")
        self.disconnect_button = QtWidgets.QPushButton("Disconnect")
        self.refresh_button = QtWidgets.QPushButton("Refresh")
        self.available_pad_list = QtWidgets.QComboBox()

        self.connect_button.clicked.connect(self.connect_pad)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.connect_button)
        layout.addWidget(self.disconnect_button)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.available_pad_list)
        self.setLayout(layout)

    @QtCore.Slot()
    def connect_pad(self):
        pass
