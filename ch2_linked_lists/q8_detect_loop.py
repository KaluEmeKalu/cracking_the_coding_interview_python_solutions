import unittest


class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


    def has_loop(self):
        """ Must run from root"""
        set_a = set()
        current = self

        while current:
            if current in set_a:
                return current
            set_a.add(current)
            current = current.next

        return False


class TestNode(unittest.TestCase):
    def test_has_loop(self):
        a = Node('H')
        b = Node('a')
        c = Node('n')
        d = Node('d')
        e = Node('y')

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = b

        self.assertEqual(b, a.has_loop())

        a = Node('H')
        b = Node('a')
        c = Node('n')
        d = Node('d')
        e = Node('y')

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        self.assertFalse(a.has_loop())

if __name__ == "__main__":
    unittest.main()

