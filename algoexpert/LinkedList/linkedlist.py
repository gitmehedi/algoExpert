class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, value, position):
        pass

    def delete(self, value):
        current = self.head

        if current.data == value:
            self.head = current.next
        else:
            while current:
                if current.data == value:
                    break
                prev = current
                current = current.next

            if current == None:
                return
            prev.next = current.next
            current = None

    def traverse(self):
        pass

    def sort(self):
        pass

    def search(self, value):
        pass

    def print_list(self):
        vals = []
        current = self.head
        while current:
            vals.append(current.data)
            current = current.next
        print(vals)


linked_list = LinkedList()

list_val = [90, 23, 7, 23, 91, 34, 23, 'Bangladesh', 'India', 'Japan', 12]
for val in list_val:
    linked_list.append(val)

linked_list.print_list()
linked_list.delete(7)
linked_list.delete(90)
linked_list.delete(12)
linked_list.print_list()
