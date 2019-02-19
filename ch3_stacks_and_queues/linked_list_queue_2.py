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

class testQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        for n in range(4,10):
            self.q.enqueue(n)

    def testDequeue(self):
        self.assertEqual(4, self.q.dequeue())
        self.assertEqual(5, self.q.dequeue())
        self.assertEqual(6, self.q.dequeue())
        self.q.enqueue(10)
        self.q.enqueue(11)
        self.assertEqual(7, self.q.dequeue())
        self.assertEqual(8, self.q.dequeue())
        self.assertEqual(9, self.q.dequeue())
        self.assertEqual(10, self.q.dequeue())
        self.assertEqual(11, self.q.dequeue())

        self.assertTrue(self.q.is_empty())


    def testPrintQ(self):
        self.q.print_q()

if __name__ == "__main__":
    unittest.main()
