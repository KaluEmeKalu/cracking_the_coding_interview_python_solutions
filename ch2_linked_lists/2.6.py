# Implement a function to check if a linked list is a palindrome
# I used the reverse method to solve.

import unittest



class LinkedList():
    def __init__(self, head):
        self.head = head

    def __repr__(self):
        return self.head.__repr__()


    def get_count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def get_mid(self):
        """ Get's ceiling of mid way point"""
        mid = self.get_count() / 2
        mid = int(mid + .5)
        return mid

    def reverse(self):
        node = Node(self.head.value, None)
        previous = self.head
        current = previous.next

        while current:

            node = Node(current.value, node)


            previous = current
            current = current.next




        reversed_linked_list = LinkedList(node)
        return reversed_linked_list


    def is_palindrome(self):
        current1 = self.head
        current2 = self.reverse().head

        while current1:
            valueIsEqual = current1.value == current2.value
            if not valueIsEqual:
                return False
            current1 = current1.next
            current2 = current2.next
        return True


class Node():
    def __init__(self, value, _next=None):
        self.value, self.next = value, _next

    def __repr__(self):
        current = self
        hold = []
        while current:
            hold.append(f'{current.value} --> ')
            current = current.next

        num_string = "".join(hold)
        return num_string


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        d = Node("t")
        c = Node("a", d)
        b = Node("o", c)
        a = Node("b", b)
        self.boat = LinkedList(head=a)

        e = Node("p")
        d = Node("e", e)
        c = Node("a", d)
        b = Node("e", c)
        a = Node("p", b)
        self.peaep = LinkedList(head=a)

    def testCanPrint(self):
        print(self.boat)
        print(self.peaep)

    def testCanGetCount(self):
        self.assertEqual(self.boat.get_count(), 4)


    def testCanGetMid(self):
        self.assertEqual(self.peaep.get_mid(), 3)

    def testPalindrome(self):
        
        self.assertEqual(False, self.boat.is_palindrome())
        self.assertEqual(True, self.peaep.is_palindrome())

    def testReverse(self):
        print("here is reverse")
        print(self.boat.reverse())

unittest.main()

