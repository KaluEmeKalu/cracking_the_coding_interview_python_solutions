# Baisc Queue
import unittest


class Queue():
    def __init__(self):
        self._array = [None] * 10
        self.count = 0
        self.front = 1

    def enqueue(self, element):
        self._array[self.count + 1] = element
        self.count += 1


    def dequeue(self):
        if self.count == 0:
            raise Exception("Sorry homie. Queue Empty.")

        element = self._array[self.front]
        self._array[self.front] = None
        self.front += 1
        self.count -= 1

        if self.count == 0:
            print(f"\n\n\nHere is count: {self.count}\n\n")
            self.front = 1
        return element

    def __repr__(self):
        return self._array.__repr__()


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        self.q.enqueue(4)
        self.q.enqueue(5)
        self.q.enqueue(6)

    def testPrintQueue(self):
        print('yo')
        print(self.q)

    def testDequeue(self):
        self.assertEqual(self.q.dequeue(), 4)
        self.assertEqual(self.q.dequeue(), 5)
        self.assertEqual(self.q.dequeue(), 6)
        self.assertRaises(Exception, self.q.dequeue)

        print("print new")
        self.q.enqueue(17)
        print(f"Here is array: {self.q}, Here is front: {self.q.front}")
        self.assertEqual(self.q.dequeue(), 17)
        print(self.q)


if __name__ == "__main__":
    unittest.main()
