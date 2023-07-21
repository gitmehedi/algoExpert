"""
Merge Linked List
"""

lsn = [13, 12, 11, 3, 5, 1, 2, 7, 6, 8]
lsn = [1, 1, 2]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def mergeList(self):
        vals = []
        sum = 0
        current = self.head
        while current:
            vals.append(current.data)
            sum = sum + current.data
            current = current.next

        print(sum)
        valint = int("".join([str(i) for i in vals]), 2)
        print(valint)

    def print_tree(self):
        vals = []
        current = self.head
        while current:
            vals.append(current.data)
            current = current.next
        print(vals)


build = ListNode()

for val in lsn:
    build.insert(val)
build.print_tree()
build.removeDuplicates()
build.print_tree()
