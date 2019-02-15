# Making a Basic Queue Structure
import unittest


class Queue():
    def __init__(self):
        self._dict = {}
        self.count = 0
        self.front = 1

    def is_empty(self):
        return len(self._dict) == 0


    def enqueue(self, element):
        self.count += 1
        self._dict[self.count] = element


    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        # import pdb; pdb.set_trace()
        item = self._dict[self.front]
        del self._dict[self.front]
        self.front += 1

        return item

    def __repr__(self):
        return self._dict.__repr__()




class testQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        self.q.enqueue(4)
        self.q.enqueue(6)

    # def testRepr(self):
    #     print(self.q)


    def testDequeue(self):
        b = Queue()
        for num in range(5, 30, 5):
            b.enqueue(num)
        self.assertEqual(5, b.dequeue())
        self.assertEqual(10, b.dequeue())
        self.assertEqual(15, b.dequeue())
        self.assertEqual(20, b.dequeue())
        self.assertEqual(25, b.dequeue())

        self.assertRaises(Exception, b.dequeue)




if __name__ == "__main__":
    unittest.main()
