import unittest


class Queue():
    def __init__(self):
        self.stack = Stack()
        self.reverse_stack = Stack()


    def enqueue(self, element):
        self.stack.push(element)


    def dequeue(self):
        while not self.stack.is_empty():
            self.reverse_stack.push(self.stack.pop())
        popped = self.reverse_stack.pop()
        return popped


class Stack():
    def __init__(self):
        self._array = []

    def is_empty(self):
        if self._array:
            return False
        return True


    def push(self, element):
        self._array.append(element)


    def pop(self):
        return self._array.pop()


    def __repr__(self):
        return self._array.__repr__()

class TestStackQueue(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push(7)
        self.stack.push(8)
        self.stack.push(9)

        self.q = Queue()
        self.q.enqueue(7)
        self.q.enqueue(8)
        self.q.enqueue(9)
        self.q.enqueue(10)


    def testArrayPop(self):
        self.assertEqual(9, self.stack.pop())
        self.assertEqual(8, self.stack.pop())
        self.assertEqual(7, self.stack.pop())

    def testDequeue(self):
        self.assertEqual(7, self.q.dequeue())







if __name__ == "__main__":
    unittest.main()