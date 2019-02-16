# Create a sort that can sort elements
import unittest
class Stack():
    def __init__(self):
        self._array = []


    def bubble_sort(self, _list):
        """ First try with regular list. After with stack/node"""
        
        n = len(_list)
        for i in range(n - 1):

            for j in range(n - i - 1):
                if _list[j] > _list[j+1]:
                    _list[j], _list[j+1] = _list[j+1], _list[j]

        return _list



    def push(self, element):
        self._array.append(element)

    def pop(self):
        popped = self._array.pop()
        return popped

    def is_empty(self):
        if self.__array:
            return False
        return True


class Node():
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return self.data.__repr__()

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push(Node(14))


        self.test_list = [18, 20, 35, -5, 299, -43]

    def testElementSavedInStack(self):
        num = self.stack.pop().data
        self.assertEqual(14, num)


    def testBubbleSortWithRegularList(self):

        sorted_list = sorted(self.test_list)
        bubble_sorted_list = self.stack.bubble_sort(self.test_list)
        self.assertEqual(bubble_sorted_list, sorted_list)




if __name__ == '__main__':
    unittest.main()