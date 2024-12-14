class Stack():
    def __init__(self,max):
        self.max = max
        self.stack = []

    def push(self,n):
        if len(self.stack) >= self.max:
            print("Stack is full")
        else:
            self.stack.append(n)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:    
            return self.stack.pop()

    def top(self):
        print(self.stack[-1])
    
    def rear(self):
        print(self.stack[0])
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print(self.stack)
        
stack = Stack(7)
stack.push(5)
stack.push(6)
stack.push(13)
stack.push(27)
stack.push(36)
stack.push(47)
print(stack.pop())
stack.top()
stack.rear()
stack.size()
stack.display()


        