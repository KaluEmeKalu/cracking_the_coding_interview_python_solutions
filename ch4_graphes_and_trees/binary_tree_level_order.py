import unittest


class Queue():
    def __init__(self):
        self.last = None
        self.first = None

    class Node():
        def __init__(self, data):
            self.data = data
            self.next = None

    def is_empty(self):
        return self.first is None

    def enqueue(self, data):
        node = self.Node(data)
        if not self.first:
            self.first = node
        if self.last:
            self.last.next = node
        self.last = node


    def dequeue(self):
        if self.is_empty():
            return Exception("Cannot dequeue an empty queue")
        element = self.first
        self.first = self.first.next
        return element.data


    def print_q(self):
        if self.is_empty():
            return ""
        hold = []
        current = self.first
        while current:
            hold.append(str(current.data))
            current = current.next
        string = "".join(hold)
        print(string)




class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return self.data.__repr__()


    @staticmethod
    def level_order_traversal(root):
        if root is None:
            return None

        work_q = Queue()
        work_q.enqueue(root)
        ans_q = Queue()

        while not work_q.is_empty():
            current = work_q.dequeue()
            ans_q.enqueue(current)
            if current.left:
                work_q.enqueue(current.left)

            if current.right:
                work_q.enqueue(current.right)

        ans_q.print_q()

class testLevelOrderPrint(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.two = Node(2)
        self.three = Node(3)
        self.four = Node(4)
        self.five = Node(5)
        self.root.left = self.two
        self.root.right = self.three
        self.two.left = self.four
        self.two.right = self.five


    def testLevelOrder(self):
        Node.level_order_traversal(self.root)
        Node.level_order_traversal(self.root)


if __name__ == "__main__":
    unittest.main()