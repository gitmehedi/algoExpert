"""
Min Max Stack Construction
"""


class MinMaxStack:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return False

    def push(self, number):
        self.stack.append(number)

    def getMin(self):
        return min(self.stack)

    def getMax(self):
        return max(self.stack)
