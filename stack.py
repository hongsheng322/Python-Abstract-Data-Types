class Stack():
    def __init__(self):
        self.top = -1
        self.data = []
    def push(self,val):
        self.data.append(val)
        self.top += 1
    def pop(self):
        val = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return val
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def Peek(self):
        if self.isEmpty():
            return None
        else:
            return self.data[self.top]

test = Stack()
test.push(5)
test.push(6)
test.push(9)
print(test.Peek())
print(test.pop())
print(test.Peek())
print(test.pop())
print(test.Peek())
print(test.pop())
print(test.Peek())
