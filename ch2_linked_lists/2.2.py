# Implement an algorithm to find the kth to last element of a singly linked list. 
import unittest

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @staticmethod
    def get_count(head):
        current = head
        count = 0
        if not head:
            return 0
        while current:
            count+=1
            current = current.next
        return count



    @staticmethod
    def find_kth_to_last_element(head, kth):
        n = Node.get_count(head)
        current = head
        index_desired = n - kth + 1
        print(f"\n\nHere is the desired index {index_desired}\n\n")

        index = 0
        while current:
            index += 1

            if index == index_desired:
                print(current.value)
                return current
            current = current.next
        Exception("Could Not find {kth} Element")

    





class TestNode(unittest.TestCase):
    def setUp(self):
        self.e = Node(20)
        self.d = Node(21, self.e)
        self.c = Node(22, self.d)
        self.b = Node(23, self.c)
        self.a = Node(24, self.b)
        self.head = Node(25, self.a)

    def testCount(self):
        count = Node.get_count(self.head)
        self.assertEqual(count, 6)

    def test_can_correctly_store_nodes(self):
        head = self.head
        current = head
        previous = None
        while current:
            if previous:
                self.assertNotEqual(previous.value, current.value)
            self.assertTrue(current.value in range(20,26))
            previous = current
            current = current.next

    def test_can_find_kth_element(self):
        d = Node.find_kth_to_last_element(self.head, 2)
        b = Node.find_kth_to_last_element(self.head, 4)
        self.assertEqual(b, self.b)

unittest.main()
