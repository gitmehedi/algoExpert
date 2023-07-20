class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class TreeBuilder:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curNode):
        if data < curNode.data:
            if curNode.left:
                self._insert(data, curNode.left)
            else:
                curNode.left = Node(data)
        else:
            if curNode.right:
                self._insert(data, curNode.right)
            else:
                curNode.right = Node(data)

    def print_tree(self, node=None):
        vals = []

        if node is None:
            node = self.root

        if node.left:
            vals = self.print_tree(node.left)

        vals.append(node.data)

        if node.right:
            vals += self.print_tree(node.right)

        return vals


nodelist = [9, 8, 7, 90, 23, 98, 4, 5, 61, 0, 3]
node = TreeBuilder()

for val in nodelist:
    node.insert(val)

sorts = node.print_tree()
print(sorts)
