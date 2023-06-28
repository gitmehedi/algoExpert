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
