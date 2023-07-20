class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def print_tree(self):
        vals = []
        if self.left:
            vals = self.left.print_tree()
        vals.append(self.data)
        if self.right:
            vals += self.right.print_tree()

        return vals


nodelist = [9, 8, 7, 90, 23, 98, 4, 5, 61, 0, 3]
node = Node()

for val in nodelist:
    node.insert(val)

sorts = node.print_tree()
print(sorts)