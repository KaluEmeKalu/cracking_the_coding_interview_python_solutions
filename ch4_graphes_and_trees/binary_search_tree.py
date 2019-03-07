import unittest


class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def in_order_traversal(node):
        if node:
            Node.in_order_traversal(node.left)
            print(node.data)
            Node.in_order_traversal(node.right)

    @staticmethod
    def pre_order_traversal(node):
        if node:
            print(node.data)
            Node.in_order_traversal(node.left)
            Node.in_order_traversal(node.right)

    @staticmethod
    def post_order_traversal(node):
        if node:
            Node.post_order_traversal(node.left)
            Node.post_order_traversal(node.right)
            print(node.data)

    @staticmethod
    def get_count(node):
        if node:
            left_count = Node.get_count(node.left)
            right_count = Node.get_count(node.right)
            return 1 + left_count + right_count
        return 0


class TestTreeNode(unittest.TestCase):
    def setUp(self):
        self.a = Node(10)
        self.b = Node(12)
        self.c = Node(13)
        self.d = Node(14)
        self.e = Node(19)
        self.f = Node(20)

        self.c.left = self.b
        self.b.left = self.a
        self.c.right = self.d
        self.d.right = self.e
        self.e.left = Node(16)
        self.e.right = self.f

    # def testInOrder(self):
    #     print("\nrunning in order")
    #     self.c.in_order_traversal(self.c)
    #     print("\nfinished in order\n")

    # def testPreOrder(self):
    #     print("\nrunning pre order")
    #     self.c.pre_order_traversal(self.c)
    #     print("\nfinished pre order\n")

    def testPostOrder(self):
        print("\nrunning post order")
        self.c.post_order_traversal(self.c)
        print("\nfinished post order\n")

    def testCount(self):
        self.assertEqual(7, self.c.get_count(self.c))



if __name__ == "__main__":
    unittest.main()