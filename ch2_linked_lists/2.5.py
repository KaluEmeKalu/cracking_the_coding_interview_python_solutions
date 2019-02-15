# Sum Lists: You have two numbers represented by a linked list, 
# where each node contains a single digit. 
# The digits are stored in reverse order, such that 
# the 1's digit is at the head of the head of hte list. 
# Write a function that adds the two numbers and returns the 
# sum as a linked list.
import unittest

class LinkedList():
    def __init__(self, head):
        self.head = head


    def get_number(self):

        current = self.head
        hold = []
        while current:
            hold.append(f'{current.value}')
            current = current.next

        hold = reversed(hold)
        num_str = "".join(hold)
        num = int(num_str)
        return num

    def add_number(self, second_linked_list):
        num1 = self.get_number()
        num2 = second_linked_list.get_number()
        return num1 + num2


    def __repr__(self):
        if self.head:
            return self.head.__repr__()


class Node():
    def __init__(self, value, _next=None):
        self.next, self.value = _next, value

    
    def __repr__(self):
        if self.value:
            current = self
            hold_list = []
            while current:
                if current.value:
                    hold_list.append(f"{current.value} --> ")
                current = current.next
            return "".join(hold_list)


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        c = Node(9)
        b = Node(5, c)
        a = Node(2, b)
        self.linked_list1 = LinkedList(head=a)
        c = Node(3)
        b = Node(7, c)
        a = Node(1, b)
        self.linked_list2 = LinkedList(head=a)


    def test_can_print_linked_list(self):
        print(self.linked_list2)
        print(self.linked_list1)

    def test_can_get_number(self):
        self.assertEqual(self.linked_list1.get_number(), 952)

    def test_add_number(self):
        ans = self.linked_list1.add_number(self.linked_list2)
        self.assertEqual(ans, 952 + 371)




unittest.main()
