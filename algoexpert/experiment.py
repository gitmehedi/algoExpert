class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, data):
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

    def print_list(self):
        vals = []
        current = self.root
        while current:
            vals.append(current.data)
            current = current.next

        print(vals)


class Solution:
    def mergeTwoList(self, list1, list2):
        head = Node(0)
        current = head

        cur1 = list1.root
        cur2 = list2.root
        while cur1.next and cur2.next:
            if cur1.data > cur2.data:
                current.next = cur1.next
                cur1 = cur1.next
            else:
                current.next = cur2.data
                cur2 = cur2.next
            current = current.next

        current.next = cur1 or cur2
        return head.next


build = LinkedList()
build2 = LinkedList()
list1 = [1, 2, 4]
list2 = [1, 3, 4]
for val in list1:
    build.insert(val)

for val2 in list2:
    build2.insert(val2)

build.print_list()
build2.print_list()

solution = Solution()
solution.mergeTwoList(build, build2)
