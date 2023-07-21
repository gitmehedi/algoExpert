"""
Remove Duplicates from Linked List
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

    def reverseList(self):
        new_list = None
        current = self.head
        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        self.head = new_list

    def removeDuplicates(self):
        current = self.head
        prev = None
        lst = []
        while current:
            if current.data not in lst:
                lst.append(current.data)
                prev = current
            else:
                prev.next = current.next
            current = current.next

    def removeDuplicate(self):
        if self.head is None:
            return False

        current = self.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

        return self.head

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
