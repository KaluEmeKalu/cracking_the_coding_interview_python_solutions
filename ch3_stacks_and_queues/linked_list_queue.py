import unittest

class LinkedList():
    def __init__(self, head=None):
        self.head = head
        self.last = None

    def is_empty(self):
        return self.head is None

    def print_linked_list(self):
        if self.is_empty():
            return ""
        hold = []
        current = self.head
        while current:
            hold.append(str(current.data))
            current = current.next
        return "".join(hold)


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue():
    def __init__(self):
        self.list = LinkedList()

    def is_empty(self):
        return self.list.is_empty()

    def enqueue(self, element):
        node = Node(element)
        if not self.list.head:
            self.list.head = node
        if self.list.last:
            self.list.last.next = node
        self.list.last = node

    def dequeue(self):
        if self.is_empty():
            return Exception("Can't dequeue and empty Queue.")
        element = self.list.head
        self.list.head = self.list.head.next
        return element.data

    def print_queue(self):
        print(self.list.print_linked_list())

class testQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        self.q.enqueue(4)
        self.q.enqueue(5)
        self.q.enqueue(6)
        self.q.enqueue(7)
        self.q.enqueue(8)

    def testLinkedList(self):
        l = LinkedList(Node(3))
        l.head.next = Node(4)
        l.head.next.next = Node(5)
        print(l.print_linked_list())

    def testPrintQ(self):
        print(self.q.print_queue())

    def testDeqeue(self):
        self.assertEqual(self.q.dequeue(), 4)
        self.assertEqual(self.q.dequeue(), 5)
        self.assertEqual(self.q.dequeue(), 6)
        self.q.enqueue(9)
        self.assertEqual(self.q.dequeue(), 7)
        self.assertEqual(self.q.dequeue(), 8)
        self.assertEqual(self.q.dequeue(), 9)
        self.assertTrue(self.q.is_empty())
        print

if __name__ == "__main__":
    unittest.main()
