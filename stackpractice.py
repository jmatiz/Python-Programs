class stack: #LIFO: last in first out
    def __init__(self):
        self.stack = []
    def push(self, value): #add a value

        if value not in self.stack:
            self.stack.append(value)
            return True
        else:
            return False
        
    def pop(self): #remove last added value
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return ("There is nothing to pop out of this empty stack!")

    def peek(self): #look at top of stack
        if len(self.stack) > 0:
            print(self.stack[-1])
        else:
            print("There is nothing to peek in this empty stack!")
    
        

teststack = stack()

teststack.push("Mon")
teststack.push("Tue")
teststack.peek()
print(teststack.pop())
teststack.peek()
