# Create a sort that can sort elements
import unittest


class Stack():
    def __init__(self):
        self._array = []

    def sort(self):
        hold = Stack()

        while not self.is_empty():
            temp = self.pop()
            while not hold.is_empty() and hold.peek() > temp:
                self.push(hold.pop())
            hold.push(temp)

        while not hold.is_empty():
            self.push(hold.pop())
        print(self)

    def peek(self):
        return self._array[-1]

    def push(self, element):
        self._array.append(element)

    def pop(self):
        popped = self._array.pop()
        return popped

    def is_empty(self):
        if self._array:
            return False
        return True

    def __repr__(self):
        return self._array.__repr__()


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push(14)
        self.stack.push(4)
        self.stack.push(34)
        self.stack.push(24)
        self.stack.push(7)

    def testPeek(self):
        peek = self.stack.peek()
        self.assertEqual(peek, 7)

    def testSort(self):
        tmp = float('inf')
        self.stack.sort()
        while not self.stack.is_empty():
            self.assertGreaterEqual(tmp, self.stack.pop())

    def testIsEmpty(self):
        b = Stack()
        self.assertTrue(b.is_empty())
        b.push(3)
        self.assertFalse(b.is_empty())

    def testPop(self):
        num = self.stack.pop()
        self.assertEqual(7, num)


if __name__ == '__main__':
    unittest.main()
