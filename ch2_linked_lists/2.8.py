# Loop Detection
import unittest

class LinkedList():
    def __init__(self, head):
        self.head = head

    def __repr__(self):
        string = f"Linked List: Head --> {self.head.__repr__()}"
        return string


    def detect_loop(self):
        d = set()

        current = self.head
        while current:
            if current not in d:
                d.add(current)
                current = current.next
            else:
                return current



class Node():
    def __init__(self, value, _next=None):
        self.value, self.next = value, _next

    def __repr__(self):
        return self.value
        # hold = []
        # current = self
        # while current:
        #     hold.append(f"{current.value} --> ")
        #     current = current.next

        # return "".join(hold)


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        e = Node('e')
        d = Node('d', e)
        c = Node('c', d)
        b = Node('b', c)
        self.a = Node('a', b)

        f = Node('f', c)
        e.next = f
        self.linked_list = LinkedList(self.a)

    def testRepr(self):
        print(self.linked_list)

    def testDetectLoop(self):
        loop_start = self.linked_list.detect_loop()
        print(loop_start)


unittest.main()