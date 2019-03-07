import unittest


class LinkedList():
    def __init__(self):
        self.head = None
        self.last = None

    def __repr__(self):
        hold = []
        current = self.head
        while current:
            hold.append(f"{current.data.__repr__()} --> ")
            current = current.next
        return "".join(hold)

    class Node():
        def __init__(self, data):
            self.data = data
            self.next = None

    def add(self, data):
        node = self.Node(data)
        if not self.head:
            self.head = node
        if self.last:
            self.last.next = node
        self.last = node

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def get(self, index):
        if index < 1:
            return ValueError("Index must be >= 1")
        current = self.head
        i = 1
        while i < index:
            current = current.next
            i += 1
        return current.data

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

    def group_by_level(self, root):
        lists = LinkedList()
        return self.group_by_level_recur(root, lists, 1)
        return lists

    @staticmethod
    def group_by_level_recur(root, lists, level):
        if root is None:
            return

        if level > lists.size():
            _list = []
            lists.add(_list)
        else:
            _list = lists.get(level)
        _list.append(root.data)
        Node.group_by_level_recur(root.right, lists, level +1)
        Node.group_by_level_recur(root.left,lists, level +1)
        return lists





class testLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        for num in range(4, 10):
            self.ll.add(num)

        self.root = Node(1)
        self.two = Node(2)
        self.three = Node(3)
        self.four = Node(4)
        self.five = Node(5)

        self.root.left = self.two
        self.root.right = self.three
        self.two.left = self.four
        self.two.right = self.five


        b = self.root.group_by_level(self.root)
        print(b)

    def testGet(self):
        self.assertEqual(4, self.ll.get(1))
        self.assertEqual(6, self.ll.size())
        print(self.ll)




if __name__ == "__main__":
    unittest.main()
