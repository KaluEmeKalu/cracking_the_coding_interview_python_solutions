import unittest


class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def print_num(self):
        current = self
        l = []
        while current:
            l.append(f"{current.value} -->")
            current = current.next

        print( "".join(l))

    def get_num(self):
        """Must call from root"""
        l = []
        current = self
        while current:
            l.append(str(current.value))
            current = current.next

        l = list(reversed(l))
        string = "".join(l)
        return int(string)

    @staticmethod
    def num_to_ll( num):
        string = str(num)
        num_list = list(string)

        current = Node(int(num_list.pop()))
        root = current

        while num_list:
            node = Node(int(num_list.pop()))
            current.next = node
            current = node
        return root


        
    def get_sum(self, other_ll):
        num1 = self.get_num()
        num2 = other_ll.get_num()
        _sum = num1 + num2

        return Node.num_to_ll(_sum)


class TestNode(unittest.TestCase):
    def setUp(self):
        self.root = Node(4)
        a = Node(3)
        b = Node(7)
        self.root.next = a
        a.next = b

        self.root2 = Node(8)
        a = Node(3)
        b = Node(9)
        self.root2.next = a
        a.next = b


    def test_get_num(self):
        self.assertEqual(self.root.get_num(), 734)

    def test_num_to_ll(self):
        node = Node.num_to_ll(324)

        current = node
        while current:
            print(current.value)
            current = current.next

    def test_add_sum(self):
        res = self.root.get_sum(self.root2)
        self.assertEqual(self.root.get_num() + self.root2.get_num(), res.get_num())



if __name__ == "__main__":
    unittest.main()

