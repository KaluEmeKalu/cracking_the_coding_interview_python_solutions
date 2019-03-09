import unittest
import random

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root=None):
        self.root = root


    def in_order(self):
        return self.in_order_recur(self.root)

    def in_order_recur(self, node):
        if node:
            for val in self.in_order_recur(node.left):
                yield val
            yield node.value
            for val in self.in_order_recur(node.right):
                yield val

    def bst_from_arr(self, arr):
        n = len(arr)
        if n == 1:
            return Node(arr[0])
        if n == 0:
            return None

        mid = n // 2
        node = Node(arr[mid])
        left_half = arr[:mid]
        right_half = arr[mid + 1:]

        node.left = self.bst_from_arr(left_half)
        node.right = self.bst_from_arr(right_half)
        return node

class TestTree(unittest.TestCase):
    def setUp(self):
        self.arr = []
        while len(self.arr) != 20:
            num = random.randint(1, 100)
            if num not in self.arr:
                self.arr.append(num)

        self.T = Tree()
        self.T.root = self.T.bst_from_arr(self.arr)


    def test_tree(self):
        res = list(self.T.in_order())
        self.assertEqual(res, self.arr)



if __name__ == "__main__":
    unittest.main()

