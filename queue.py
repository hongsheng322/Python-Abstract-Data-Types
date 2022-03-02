class Queue():
    def __init__(self):
        self.rear = -1
        self.data = []
    def Enqueue(self, val):
        self.data.append(val)
        self.rear += 1
    def Dequeue(self):
        val = self.data[0]
        del self.data[0]
        self.rear -= 1
        return val
    
    