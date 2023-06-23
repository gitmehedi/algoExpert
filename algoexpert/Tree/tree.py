class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inOrderTraverse(self, root):
        res = []
        if root:
            res = self.inOrderTraverse(root.left)
            res.append(root.data)
            res = res + self.inOrderTraverse(root.right)
        return res

    def preOrderTraverse(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrderTraverse(root.left)
            res = res + self.preOrderTraverse(root.right)
        return res

    def postOrderTraverse(self, root):
        res = []
        if root:
            res = self.postOrderTraverse(root.left)
            res = res + self.postOrderTraverse(root.right)
            res.append(root.data)
        return res

    def printTree(self):
        list = []

        if self.left:
            self.left.PrintTree()

        list.append(self.data)

        if self.right:
            self.right.PrintTree()

        return list


root = Node(10)
vals = [23, 45, 61, 23, 4, 67, 23, 6, 45, 34, 12, 45, 1, 3, 4, 6, 78, 2, 3, 12, 45, 23, 56, 7, 23]
for val in vals:
    root.insert(val)
print(root.inOrderTraverse(root))
print(root.preOrderTraverse(root))
print(root.postOrderTraverse(root))
