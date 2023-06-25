class Queue:
    def __init__(self):
        self.queue = []

    def add(self, data):
        self.queue.insert(0, data)

    def remove(self):
        lst = []
        for _ in self.queue:
            lst.append(self.queue.pop())
        print(lst)

    def peek(self):
        return self.queue[-1]

    def print_stack(self):
        print(self.queue)


aStack = Queue()
vals = [4, 3, 12, 32, 1, 2]
for val in vals:
    aStack.add(val)

# print(aStack.peek())
aStack.print_stack()
print(aStack.remove())
# aStack.print_stack()
