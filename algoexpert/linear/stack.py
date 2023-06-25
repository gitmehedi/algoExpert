class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        self.stack.append(data)

    def remove(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return False

    def peek(self):
        return self.stack[-1]

    def print_stack(self):
        print(self.stack)


aStack = Stack()
vals = [4, 3, 12, 32, 1, 2]
for val in vals:
    aStack.add(val)
print(aStack.peek())
aStack.print_stack()
aStack.remove()
aStack.print_stack()
