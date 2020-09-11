class RingBuffer:
    def __init__(self, capacity=10):
        self.data = [None for i in range(capacity)]

    def append(self, item):
        self.data.pop(0)
        self.data.append(item)

    def get(self):
        return self.data

