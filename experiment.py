"""
Stack Array Implementation
"""

from sys import maxsize


def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")


def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)

    return stack.pop()


def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)  # return minus infinite
    return stack[len(stack) - 1]


stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack))

"""
Stack Linked List Implementation
"""


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.root = None

    def push(self, elm):
        new_node = StackNode(elm)
        new_node.next = self.root
        self.root = new_node

    def pop(self):
        if self.root is None:
            return []
        temp = self.root
        self.root = self.root.next

        return temp.data

    def peek(self):

        return self.root.data if self.root else None

    def showStack(self):
        res = []
        current = self.root
        while current:
            res.append(current.data)
            current = current.next
        return res


stack = Stack()
stack.push(5)
stack.push(15)
stack.push(35)
stack.push(55)
stack.push(75)
print(stack.showStack())
print(stack.pop())
print(stack.showStack())
print(stack.pop())
print(stack.showStack())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.peek())
print(stack.showStack())
