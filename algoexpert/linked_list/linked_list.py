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

    """
    AlgoExpert
    ==========
    Remove Duplicates from LinkedList
    """

    def removeDuplicate(self):
        current = self.head
        prev = None
        lst = []

        while current is not None:
            if current.data not in lst:
                lst.append(current.data)
                prev = current
            else:
                current = current.next
                prev.next = current

    """
    AlgoExpert
    ==========
    """

    def print_list(self):
        vals = []
        current = self.head
        while current:
            vals.append(current.data)
            current = current.next
        print(vals)


linked_list = LinkedList()

list_val = [90, 23, 7, 23, 91, 34, 23, 'Bangladesh', 'India', 'Japan', 12]
# list_val = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
for val in list_val:
    linked_list.append(val)

linked_list.print_list()
# linked_list.delete(7)
# linked_list.delete(90)
# linked_list.delete(12)
linked_list.removeDuplicate()
linked_list.print_list()


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class BuildLinked:
    def __init__(self):
        self.root = None

    def append(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while current.next:
                current = current.next
            current.next = new_node

    def addSorting(self, data):
        new_node = Node(data)
        if self.root:
            if self.root.data > data:
                new_node.next = self.root
                self.root = new_node
            else:
                current = self.root
                while current.next:
                    if current.next.data > data:
                        break
                    current = current.next
                new_node.next = current.next
                current.next = new_node
        else:
            self.root = new_node

    def delete(self, data):
        if self.root is None:
            return False

        current = self.root
        while current.next:
            if current.data == data:
                current.next = current.next.next
            current = current.next

    def print_build(self):
        vals = []
        current = self.root
        while current:
            vals.append(current.data)
            current = current.next

        print(vals)


linked_list = [30, 4, 10, 2, 40, 26, 17, 11, 2, 3, 5, 6, 1]
# linked_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# linked_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linked_list = [1, 2, 4]
build = BuildLinked()
for val in linked_list:
    build.addSorting(val)

build.print_build()
build.delete(1)
build.print_build()
build.delete(3)
build.print_build()
build.delete(10)
build.print_build()
build.delete(26)
build.print_build()
build.delete(40)
build.print_build()
