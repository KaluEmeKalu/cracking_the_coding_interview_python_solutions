# Partitian

# I will make any number less than x the head
import unittest

class Node():
    def __init__(self, value, next=None):
        self.value, self.next = value, next

    @staticmethod
    def partition(head, num):

        current_head, previous = head, head
        current = previous.next

        while current:
            _next = current.next
            _previous = current.next
            if current.value < num:

                if current.next:
                    # Not the last node.
                    # Make previous.next point to current.next
                    previous.next = current.next
                    # Move current node to Head
                    current.next = current_head
                    # Set marker to know what current head is
                    current_head = current
                    
                    # Make current the previous one
                    # for next while Loop iteration
                    current = previous

                else:
                    # Last Node
                    # Move current node to head
                    current.next = current_head
                    # Make Previous node the last by 
                    # having it's next point to None
                    previous.next = None  
                    # Set marker to know what current head is
                    current_head = current 

                    # Make current the previous one
                    # for next while Loop iteration
                    current = previous              

            else:
                previous = current
                current = current.next

        return current_head




    def __repr__(self):
        if self.value:
            current = self
            string = []
            while current:
                string.append(f"{current.value} --> ")
                current = current.next
            return "".join(string)

class TestNode(unittest.TestCase):

    def setUp(self):
        self.f = Node(15)
        self.e = Node(11, self.f)
        self.d = Node(12, self.e)
        self.c = Node(23, self.d)
        self.b = Node(24, self.c)
        self.a = Node(21, self.b)


    @staticmethod
    def print_all_nodes(head):
        current = head
        while current:
            print(current.value)
            current = current.next




    def test_partition(self):
        head = Node.partition(self.a, 22)
        print("\n", head)




     


unittest.main()