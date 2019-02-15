# Remove Duplicates: Write code to remove duplicates from an unsorted linked list
import unittest

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @staticmethod
    def delete_node(head, node_to_delete):

        current_node = head
        previous_node = None

        while current_node:
            if current_node == node_to_delete:
                if current_node == head:
                    new_head = current_node.next
                    head.next = None
                    return new_head
                else:
                    previous_node.next = current_node.next
                    return head
            previous_node = current_node
            current_node = current_node.next
        raise Exception("Could not find value to delete")             

    @staticmethod
    def remove_duplicates(head):
        current_node = head
        values = set()
        while current_node:
            if current_node.value not in values:
                values.add(current_node.value)
            else:
                current_node.delete_node(head, current_node)
            current_node = current_node.next


class TestNode(unittest.TestCase):
    def setUp(self):
        self.head = Node(23)
        self.a = Node(24)
        self.b = Node(30)
        self.c = Node(24)
        self.d = Node(40)
        self.e = Node(23)

        self.head.next = self.a
        self.a.next = self.b
        self.b.next = self.c
        self.c.next = self.d
        self.d.next = self.e

    def test_can_delete_node(self):
        Node.delete_node(self.head, self.b)
        self.assertNotEqual(self.a.next, self.b)
        self.assertEqual(self.a.next, self.c)


        Node.delete_node(self.head, self.head)
        self.assertEqual(self.head.next, None)
    def test_remove_duplicates(self):
        Node.remove_duplicates(self.head)
        self.assertEqual(self.d.next, None)
        self.assertEqual(self.b.next, self.d)

    def test_can_print_all_node_values(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next






unittest.main()




