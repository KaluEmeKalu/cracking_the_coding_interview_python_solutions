# Implement a function to check if a linked list is a palindrome
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


    def is_palindrome(self):

        current = self.head
        index = 1
        n = self.get_count()

        first = True
        while index <= self.get_mid():
            if first:
                ahead = current.next

            print("\n", index, current)
            print(f"Here is current.next: {current.next}\n\n")
            j = 1
            for _ in range(n - index - 1):
                j += 1
                ahead = ahead.next
            print(f"Ran for loop from 1 to {j}")
            print(f" Here is ahead: {ahead}")


            index += 1
            current = current.next


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
        self.boat.is_palindrome()

unittest.main()

