import unittest

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def get_height(node):
        if node:
            left = Node.get_height(node.left)
            right = Node.get_height(node.right)
            return 1 + max(left, right)
        return -1


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
        self.assertEqual(2, self.root.get_height(self.root))
if __name__ == "__main__":
    unittest.main()
