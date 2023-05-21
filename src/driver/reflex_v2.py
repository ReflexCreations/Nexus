from multiprocessing import Process

class ReflexPadDriver(Process):
    def __init__(self):

    def run(self):
        while not self.exit.is_set():
            