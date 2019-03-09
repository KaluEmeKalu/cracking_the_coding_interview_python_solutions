import unittest


class Stack(object):
	def __init__(self):
		self._array = []


	def push(self, val):
		self._array.append(val)

	def pop(self):
		return self._array.pop()

	def __len__(self):
		return len(self._array)



class StackofPlates(object):
	def __init__(self, limit=5):
		self.stacks = [Stack()]
		self.limit = limit

	def push(self, val):
		stack = self.stacks[-1]

		if len(stack) == self.limit:
			stack = Stack()
			self.stacks.append(stack)
		stack.push(val)


	def pop(self):
		stack = self.stacks[-1]

		val = stack.pop()

		if len(stack) == 0 and len(self.stacks) != 1:
			self.stacks.pop()
		return val

		



class TestStackofStacks(unittest.TestCase):
	def setUp(self):
		stack = StackofPlates()

		stack.push(30)
		stack.push(31)
		stack.push(32)
		stack.push(33)
		stack.push(34)
		stack.push(35)
		stack.push(36)
		self.stack = stack

	def testStack(self):
		s = self.stack

		# Check That there are 2 stacks
		num_of_stacks = len(s.stacks)
		self.assertEqual(num_of_stacks, 2)

		self.assertEqual(s.pop(), 36)
		self.assertEqual(s.pop(), 35)

		# Check that there is now only 1 stack 
		num_of_stacks = len(s.stacks)
		self.assertEqual(num_of_stacks, 1)


		self.assertEqual(s.pop(), 34)
		self.assertEqual(s.pop(), 33)
		self.assertEqual(s.pop(), 32)
		self.assertEqual(s.pop(), 31)
		self.assertEqual(s.pop(), 30)



if __name__ == "__main__":
	unittest.main()