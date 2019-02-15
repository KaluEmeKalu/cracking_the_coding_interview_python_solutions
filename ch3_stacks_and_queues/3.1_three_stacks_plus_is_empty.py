# Describe how you can use a single array to implement three stacks
import unittest


class AndreThreeStacks():
    def __init__(self):
        self.array = [None, None, None]
        self.current = [0, 1, 2]


    def __repr__(self):
        return self.array.__repr__()



    def push(self, element, stack_num):
        if stack_num not in [0, 1, 2]:
            return ValueError(f"Stack num: {stack_num} does not exist.")


        if len(self.array) <= self.current[stack_num]:

            for _ in range(3):
                self.array.append(None)
        self.array[self.current[stack_num]] = element
        self.current[stack_num] += 3



    def is_empty(self, stack_num):
        if stack_num not in [0, 1, 2]:
            return ValueError(f"Stack num: {stack_num} does not exist.")

        if self.current[stack_num] >= 3:
            return False
        return True


    def pop(self, stack_num):
        if stack_num not in [0, 1, 2]:
            return ValueError(f"Stack num: {stack_num} does not exist.")

        if self.is_empty(stack_num):
            print("Stack is empty")
            return None # maybe raise error instead
        else:
            self.current[stack_num] -= 3
            element = self.array[self.current[stack_num]]
            self.array[self.current[stack_num]] = None
            return element




class testAndreThreeStacks(unittest.TestCase):
    def setUp(self):
        self.three_stacks = AndreThreeStacks()


    def testPush(self):
        self.three_stacks.push(101, 0)
        self.three_stacks.push(102, 0)
        self.three_stacks.push(201, 1)
        self.three_stacks.push(202, 1)
        self.three_stacks.push(103, 0)

        print(self.three_stacks)

    def testPop(self):
        self.three_stacks.push(101, 0)
        self.three_stacks.push(102, 0)
        self.three_stacks.push(201, 1)
        self.three_stacks.push(202, 1)
        self.three_stacks.push(103, 0)
        self.three_stacks.push(301, 2)

        popped = self.three_stacks.pop(1) 
        print(f"\nHere is the popped: {popped}\n")
        self.assertEqual(202, popped)

        popped = self.three_stacks.pop(1)
        popped = self.three_stacks.pop(0)
        popped = self.three_stacks.pop(0)
        popped = self.three_stacks.pop(2)
        popped = self.three_stacks.pop(0)
        print(f"\nAgain, here is the popped: {popped}\n")

        print(f"\nLast time is the Popped Stack: {self.three_stacks}\n")


        print(f"Here is current: {self.three_stacks.current}")







unittest.main()