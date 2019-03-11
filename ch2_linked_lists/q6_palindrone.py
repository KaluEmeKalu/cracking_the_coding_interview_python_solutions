import unittest


class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def get_string(self):
        """ Must run from root"""
        current = self
        l = []
        while current:
            l.append(current.value)
            current = current.next
        return "".join(l)

    def is_palindrone(self):
        return self._is_palindrone(self.get_string())

    @staticmethod
    def _is_palindrone(string):
        n = len(string)
        mid = int(n / 2)
        i = 0
        while i != mid:
            if string[i] != string[n - i - 1]:
                return False
            i += 1
        return True

class TestNode(unittest.TestCase):
    def testPalindrone(self):


        self.assertTrue(Node._is_palindrone('dood'))
        self.assertFalse(Node._is_palindrone('caterpillar'))


    def test_real_is_palindrone(self):
        a = Node('d')
        b = Node('o')
        c = Node('o')
        d = Node('d')
        a.next = b
        b.next = c
        c.next = d
        self.assertTrue(a.is_palindrone())

        a = Node('c')
        b = Node('a')
        c = Node('t')
        a.next = b
        b.next = c
        self.assertFalse(a.is_palindrone())



if __name__ == "__main__":
    unittest.main()