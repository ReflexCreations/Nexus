from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("RE:Flex Nexus")
        self.setMinimumSize(800, 600)

        layout = QVBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        #self.style_sheet = file_handler.load('
        self.setStyleSheet("")

    def zoom(self, value):
        font = self.font()
        font.setPointSize(12 * value / 100)
        self.setFont(font)

        padding = 10 * value / 100
        #self.setStyleSheet(stylesheet.replace(10px", f"{padding}px"))
                       
    def load_stylesheet():
        with open('stylesheet.qss', 'r') as f:
            return f.read()
        
    #def load_profile(profile):