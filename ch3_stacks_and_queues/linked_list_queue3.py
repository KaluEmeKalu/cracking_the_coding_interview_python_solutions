import unittest

class Queue():
    def __init__(self):
        self.first = None
        self.last = None

    class Node():
        def __init__(self, data):
            self.data = data
            self.next = None

    def enqueue(self, element):
        node = self.Node(element)
        if not self.first:
            self.first = node
        if self.last:
            self.last.next = node
        self.last = node

    def is_empty(self):
        return self.first == None


    def dequeue(self):
        if self.is_empty():
            return Exception("Cannot dequeue an empty queue!")
        element = self.first
        self.first = self.first.next
        return element.data


    def print_q(self):
        hold = []
        current = self.first
        while current:
            hold.append(str(current.data))
            current = current.next
        string = "".join(hold)
        print(string)

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.next

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        for num in range(4,9):
            self.q.enqueue(num)

        self.q.print_q()

    def testDequeue(self):
        self.assertEqual(4, self.q.dequeue())
        self.assertEqual(5, self.q.dequeue())
        self.assertEqual(6, self.q.dequeue())
        self.q.enqueue(9)
        self.q.enqueue(10)
        self.assertEqual(7, self.q.dequeue())
        self.assertEqual(8, self.q.dequeue())
        self.assertEqual(9, self.q.dequeue())
        self.assertEqual(10, self.q.dequeue())
        self.assertTrue(self.q.is_empty())

    def testIter(self):
        queue = Queue()
        list1 = list(range(4, 9))
        for num in list1:
            queue.enqueue(num)
        list2 = list(queue.__iter__())
        self.assertEqual(list1, list2)



if __name__ == "__main__":
    unittest.main()