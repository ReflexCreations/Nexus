import hid
from multiprocessing import Process
from ..os_interface import os_interface
from PyQt5.QtWidgets import QWidget, QComboBox, QHBoxLayout, QPushButton

PAD_USB_VID = 0x0483
PAD_USB_PID = 0x5750
PAD_PRODUCT_STRING = "RE:Flex Dance Pad"
USB_HID_PACKET_SIZE = 64

class Model():
    def __init__(self):
        self.pad = None

    def open(self, serial=None):
        self.pad = hid.device()
        self.pad.open(PAD_USB_VID, PAD_USB_PID, serial_number=serial)
        if self.pad.get_product_string() == PAD_PRODUCT_STRING:
            process = Process(target=self.io_loop, args=(serial,))
            process.start()
        self.lock_access()

    def close(self):
        self.unlock_access()
        self.pad.close()

    def lock_access(self):
        os_interface.lock_access(self.pad)

    def unlock_access(self):
        os_interface.unlock_access(self.pad)

    @staticmethod
    def enumerate():
        pad_list = [p for p in hid.enumerate(PAD_USB_VID, PAD_USB_PID)]
        return pad_list

    @staticmethod
    def io_loop(serial):
        pad = hid.device()
        pad.open(PAD_USB_VID, PAD_USB_PID, serial_number=serial)
        rx_packet = pad.read(USB_HID_PACKET_SIZE)
        print(rx_packet)

class View(QWidget):
    def __init__ (self, parent=None):
        super().__init__(parent)

        self.connect_button = QPushButton('Connect')
        self.disconnect_button = QPushButton('Disconnect')
        self.refresh_button = QPushButton('Refresh')
        self.available_pad_list = QComboBox()

        layout = QHBoxLayout()
        layout.addWidget(self.connect_button)
        layout.addWidget(self.disconnect_button)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.available_pad_list)

        self.setLayout(layout)

from .pad_interface import Model, View
from ..helper import inject, slot
from logger import logger

class Controller():
    @inject
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        
        self.connect = self.view.connect_button.clicked
        self.disconnect = self.view.disconnect_button.clicked
        self.refresh = self.view.refresh_button.clicked
    
    @slot
    def enumerate(self):
        print(self.model.enumerate())
    
    @slot
    def open(self):
        self.model.open()

    @slot
    def disconnect_clicked(self):
        logger.add_info("Disconnect clicked.")