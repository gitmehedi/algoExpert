"""
Linked List Operations
"""
ll = [1, 2, 3]


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def append(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
        else:
            current = self.root
            while current.next:
                current = current.next
            current.next = node

    def prepend(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
        else:
            node.next, self.root = self.root, node

    def insert(self, data, after):
        node = Node(data)
        if not self.root:
            self.root = node
        else:
            current = self.root
            while current.next:
                if current.data == after:
                    break
                current = current.next
            node.next = current.next
            current.next = node

    def pop(self, position=None):
        current = self.root
        prev = current
        if not position:
            while current:
                prev = current
                current = current.next
            prev.next = None
        else:
            self.root = self.root.next
    def print_ll(self):
        res = []
        current = self.root
        while current:
            res.append(current.data)
            current = current.next
        return res


pl = [5, 6, 7]
link = LinkedList()
for l in ll:
    link.prepend(l)
    link.append(l)

for p in pl:
    link.insert(p, 1)

link.pop()
link.pop()
link.pop()
link.pop(1)
link.pop(1)


print(link.print_ll())
