import unittest


class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def remove_duplicates(self):
        seen = [self.value]
        prev = self
        current = self.next
        while current:
            if current.value in seen:
                current.delete_node(prev)
            else:
                seen.append(prev.value)
            prev = current
            current = current.next
        return self


    def delete_node(self, prev):
        prev.next = self.next



class TestNode(unittest.TestCase):
    def setUp(self):
        self.root = Node(20)
        a = Node(21)
        b = Node(22)
        c = Node(23)
        d = Node(21)
        e = Node(24)
        self.root.next = a
        a.next = b
        b.next = c
        c.next = d
        d.next = e

    def testNode(self):
        self.root.remove_duplicates()

        current = self.root
        while current:
            print(current.value)
            current = current.next


if __name__ == "__main__":
    unittest.main()