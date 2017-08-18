class Data(object):
    def __init__(self, byte_data: bytes):
        self.content = byte_data

    @property
    def size(self):
        return len(self.content)