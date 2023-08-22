class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert = data
                else:
                    self.left = Node(data)

            elif data > self.data:
                if self.right:
                    self.right.insert = data
                else:
                    self.right = data
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




"""
Linked List Operations
"""


class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def depthOfTree(self):
        if self.data is None:
            return 0
        else:
            if self.left and self.right:
                lDepth = self.left.depthOfTree()
                rDepth = self.right.depthOfTree()

                if lDepth > rDepth:
                    return lDepth + 1
                else:
                    return rDepth + 1
        return 0

    def inOrderTraverse(self):
        res = []
        if self.left:
            res = self.left.inOrderTraverse()
        res.append(self.data)
        if self.right:
            res = res + self.right.inOrderTraverse()
        return res

    def preOrderTraverse(self):
        res = []
        res.append(self.data)
        if self.left:
            res = res + self.left.inOrderTraverse()
        print(res)
        if self.right:
            res = res + self.right.inOrderTraverse()
        print(res)

        return res

    def postOrderTraverse(self):
        res = []
        if self.left:
            res = self.left.postOrderTraverse()
        if self.right:
            res = res + self.right.postOrderTraverse()
        res.append(self.data)
        return res

    def sumOfBranch(self):
        if self.left is None or self.right is None:
            return []

        left = self.left.sumOfBranch()
        right = self.right.sumOfBranch()

        branch = left + right
        if branch:
            return [val+self.data for val in branch]
        else:

            return [self.data]

def branchSums(root):
    if root is None:
        return []
    left = branchSums(root.left)
    right = branchSums(root.right)
    branch = left + right
    if branch:
        return [x + root.data for x in branch]
    else:
        return [root.data]


array = [6, 5, 8, 7, 5, 3, 2, 9]
node = Tree()
node2 = Tree(6)
for n in array:
    node.insert(n)
# print(node.sumOfBranch())
# print(node.inOrderTraverse())
# print(node.postOrderTraverse())
# print(node.depthOfTree())
print(branchSums(node2))

