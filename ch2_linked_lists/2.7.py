# Intersection 
import unittest


class LinkedList():
    def __init__(self, head):
        self.head = head

    def __repr__(self):
        string = f"Linked List: {self.head.__repr__()}"
        return string

    def intersection(self, other_linked_list):

        current1 = other_linked_list.head
        current2 = self.head

        d = set()

        while current1 and current2:

            if current1 not in d:
                d.add(current1)
            else:
                print(f"\n\n\nWe have a match!!!: Current1: {current1}\n\n\n")
                return current1
            if current2 not in d:
                d.add(current2)
            else:
                print("\n\n\nWe have a match!!!\n\n\n")
                print(f"\n\n\nWe have a match!!!: Current2: {current2}\n\n\n")
                return current2

            current1 = current1.next
            current2 = current2.next


class Node():
    def __init__(self, value, _next=None):
        self.value, self.next = value, _next

    def __repr__(self):
        hold = []
        current = self
        while current:
            hold.append(f"{current.value} --> ")
            current = current.next

        return "".join(hold)


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        e = Node('e')
        d = Node("d", e)
        c = Node("c", d)
        b = Node("b", c)
        self.a = Node("a", b)

        four = Node('4', c)
        three = Node('3', four)
        two = Node('2', three)
        self.one = Node('1', two)

        self.ll1 = LinkedList(self.a)
        self.ll2 = LinkedList(self.one)

    # def testNodeRepr(self):
    #     print(self.ll1)
    #     print(self.ll2)

    def testIntersection(self):
        ans = self.ll1.intersection(self.ll2)
        print(f"Here is the answer: {ans}")


unittest.main()
