from interface import XRecordInterface

class Movement:
    def __init__(self, key):
        self.key = key

    def execute(self, interface: XRecordInterface):
        interface.send_key(self.key)