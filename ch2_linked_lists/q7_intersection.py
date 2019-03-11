import unittest

class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def intersection(self, other_ll):
        set_a = set()
        current = self

        while current:
            set_a.add(current)
            current = current.next

        current = other_ll
        while current:
            if current in set_a:
                return current
            current = current.next
        return False

class TestNode(unittest.TestCase):
    def test_intersection(self):
        root1 = Node('B')
        a = Node('o')
        b = Node('a')
        c = Node('r')
        root1.next = a
        a.next = b
        b.next = c

        root2 = Node('S')
        a = Node('t')
        root2.next = a
        a.next = b

        root3 = Node('C')
        x = Node('a')
        z = Node('t')
        root3.next = x
        x.next = z

        self.assertTrue(root1.intersection(root2))
        self.assertFalse(root1.intersection(root3))





if __name__ == "__main__":
    unittest.main()
