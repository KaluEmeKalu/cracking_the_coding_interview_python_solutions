# Implement an algorithm to dlete a node in the middle of a singly linked list
# given only access to that node
import unittest


class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



    def delete_node(self):
        self.value = self.next.value
        self.next = self.next.next
    
    @staticmethod
    def print_all_nodes(head):
        current = head

        while current:
            print(current.value)
            current = current.next


class NodeTest(unittest.TestCase):
    def setUp(self):
        self.e = Node(25)
        self.d = Node(24, self.e)
        self.c = Node(23, self.d)
        self.b = Node(22, self.c)
        self.a = Node(21, self.b)
        self.head = Node(20, self.a)

    def test_print_all_nodes(self):
        print('\n')
        Node.print_all_nodes(self.head)

    def test_can_delete_node(self):
        self.c.delete_node()
        self.assertEqual(self.c.value, self.d.value)
        self.assertEqual(self.c.next, self.e)


unittest.main()





