import PyQt5.QtWidgets as QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("RE:Flex Nexus")
        self.setMinimumSize(800, 600)
        layout = QtWidgets.QVBoxLayout()
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setStyleSheet("")

    def zoom(self, value):
        font = self.font()
        font.setPointSize(12 * value / 100)
        self.setFont(font)
        padding = 10 * value / 100
                       
    def load_stylesheet():
        with open('stylesheet.qss', 'r') as f:
            return f.read()
