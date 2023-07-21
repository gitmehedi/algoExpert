"""
Sum of Two Linked Lists
"""
lista = [2, 4, 7, 1]
listb = [9, 4, 5]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListNode:
    def __init__(self, data=None):
        self.head = data

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print_tree(self):
        vals = []
        current = self.head
        while current:
            vals.append(current.data)
            current = current.next
        print(vals)


def sum_of_lists(lista, listb):
    l1 = lista
    l2 = listb
    dummy = ListNode(None)
    carry = 0
    curr = dummy
    while l1 or l2 or carry:
        v1 = l1.data if l1.data else 0
        v2 = l2.data if l2.data else 0

        val = v1 + v2 + carry
        val = val % 10
        carry = val // 10
        curr.next = ListNode(val)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


build = ListNode()
build2 = ListNode()

for val in lista:
    build.insert(val)
for val2 in listb:
    build2.insert(val2)

build.print_tree()
build2.print_tree()
sum_of_lists(lista, listb)
build.print_tree()
