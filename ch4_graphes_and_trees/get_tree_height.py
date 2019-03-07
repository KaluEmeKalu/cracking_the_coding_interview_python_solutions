import unittest

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def get_height(self, node):
        if node is None:
            return -1
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return 1 + max(left_height, right_height)


class testNode(unittest.TestCase):
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

    def testGetHeight(self):
        self.assertEqual(1, self.root.get_height(self.two))



if __name__ == "__main__":
    unittest.main()