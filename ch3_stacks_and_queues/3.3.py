# 3.3 - Stack of Plates
import unittest

class StackofStacks():
    def __init__(self, capacity=5):
        self._full_arrays = []
        self._current_array = []
        self._capacity = capacity


    def print_stack_details(self):
        print(f"Here is full stack {self._full_arrays}")
        print(f"Here is current stack: {self._current_array}")


    def push(self, element):

        if len(self._current_array) < self._capacity:
            self._current_array.append(element)
        else:
            self._full_arrays.append(self._current_array)
            self._current_array = []
            self.push(element)

    def pop(self):

        if not self._current_array:
            print("\n\n about to raise exception \n\n")
            raise Exception("Can't Pop. No items in Stack")
        

        elif len(self._current_array) == 1:
            element = self._current_array.pop()

            if self._full_arrays:
                self._current_array = self._full_arrays.pop()
            return element
        return self._current_array.pop()
        



class testStackofStacks(unittest.TestCase):
    def setUp(self):
        self.stack = StackofStacks()
        for num in range(0, 80, 7):
            self.stack.push(num)

    # def testPrintFullArrays(self):
    #     print(self.stack._full_arrays)

    # def testPrintCurrentArray(self):
    #     print(self.stack._current_array)


    # def test_pop_throws_exception_if_stack_empty(self):
    #     s = StackofStacks()
    #     self.assertRaises(Exception, s.pop())

    def testPop(self):
        for x in range(12):

            self.stack.pop()
            self.stack.print_stack_details()

        self.assertRaises(Exception, self.stack.pop, msg="Can't Pop. No items in Stack")


            # Don't understand why exception isn't being raised
            # should be raised when x >=26
















if __name__ == "__main__":
    unittest.main()