# Stack with min, pop, and push
import unittest


class Stack():
    def __init__(self):
        self._array = []
        self._min = []
        self._second_smallest = None

    def update_min_after_push(self, node):
        """Update min if pushed element is smallest"""
        if not self._min:
            self._min.append(node)
        elif node.data < self._min[-1].data:
            self._min.append(node)

    def update_min_after_pop(self, popped_node):
        """Update min if popped element is smallest"""
        if popped_node == self._min[-1]:
            self._min.pop()

    def push(self, element):
        node = Node(element)
        self._array.append(Node(element))  # adds element to _array array
        self.update_min_after_push(node)  # add element to _min array

    def min(self):
        if not self._min:
            return None
        return self._min[-1].data

    def _pop(self):
        """ Returns Node Container of popped number"""
        popped_node = self._array.pop()
        self.update_min_after_pop(popped_node)
        return popped_node

    def pop(self):
        """ Public Method to pop.
        Returns the Data element popped w/o Node Container
        """
        return self._pop().data

    def __repr__(self):
        return self._array.__repr__()


class Node():
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return self.data.__repr__()


class testArray(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push(34)
        self.stack.push(837)
        self.stack.push(47)
        self.stack.push(-97)
        self.stack.push(89)

    def testPopStack(self):
        popped = self.stack.pop()
        self.assertEqual(popped, 89)

    def testMin(self):
        self.stack.push(-283)
        self.stack.push(323)
        self.stack.push(400)
        self.assertEqual(-283, self.stack.min())

    def testMinWorksAfterPopped(self):
        self.stack.push(-33389)
        self.assertEqual(-33389, self.stack.min())
        self.stack.pop()
        self.assertEqual(-97, self.stack.min())


if __name__ == "__main__":
    unittest.main()
