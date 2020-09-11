class RingBuffer:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.currentPOS = 0
        self.store = [None] * capacity


    def append(self, item):
        if self.capacity == self.currentPOS:
            self.currentPOS = 0 #resets back to the beginning of the list (FIFO applies once you hit the end of the list. This checks the current position, and if it is equal to the capacity {the end of the list}, it will reset the position back to 0/the first)
            self.store[self.currentPOS] = item
        
        self.store[self.currentPOS] = item
        self.currentPOS += 1
            

    def get(self):
        return [i for i in self.store if i is not None]
