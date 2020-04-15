class queue: #first in first out
    def __init__(self):
        self.queue = []
    def size(self):
        return len(self.queue)
    def addtoq(self, value):
        self.queue.insert(0,value)
    def peek(self):
        if self.size() > 0:
            print(self.queue[-1])
        else:
            print("This queue is empty!")
    def popq(self):
        if self.size() > 0:
            return self.queue.pop()
        else:
            return ("This queue is empty!")


testq = queue()

testq.addtoq("Mon")
testq.addtoq("Tue")
testq.addtoq("Wed")

print(testq.popq())
print(testq.popq())
print(testq.popq())

print(testq.size())
