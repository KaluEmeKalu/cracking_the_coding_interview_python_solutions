import unittest


class ThreeStacks(object):
	def __init__(self):
		self.next_index = [0, 1, 2]
		self.array = [None, None, None]


	def push(self, stack, val):
		n = len(self.array)
		if n <= self.next_index[stack]:
			for _ in range(3):
				self.array.append(None)

		index = self.next_index[stack]
		self.array[index] = val
		self.next_index[stack] += 3


	def pop(self, stack):
		self.next_index[stack] -= 3
		index = self.next_index[stack]
		val = self.array[index]

		self.array[index] = None

		#resize array
		while self.array and self.array[-1] == None:
			self.array.pop()

		return val



class TestStack(unittest.TestCase):

	def add_stuff(self, stack):
		stack.push(0, 'a1')
		stack.push(0, 'a2')
		stack.push(0, 'a3')
		stack.push(1, 'b1')
		stack.push(1, 'b2')
		stack.push(1, 'b3')
		stack.push(2, 'c1')
		stack.push(2, 'c2')
		stack.push(2, 'c3')
		return stack

	def setUp(self):
		stack = ThreeStacks()
		self.stack = self.add_stuff(stack)


	def test_pop(self):
		self.assertEqual(self.stack.pop(0), 'a3')
		self.assertEqual(self.stack.pop(0), 'a2')
		self.assertEqual(self.stack.pop(0), 'a1')
		self.assertEqual(self.stack.pop(1), 'b3')
		self.assertEqual(self.stack.pop(1), 'b2')
		self.assertEqual(self.stack.pop(1), 'b1')
		self.assertEqual(self.stack.pop(2), 'c3')
		self.assertEqual(self.stack.pop(2), 'c2')
		self.assertEqual(self.stack.pop(2), 'c1')

		n = len(self.stack.array)
		self.assertEqual(n, 0)

		# Do it again. To Make Sure stack still works
		self.add_stuff(self.stack)
		self.assertEqual(self.stack.pop(0), 'a3')
		self.assertEqual(self.stack.pop(0), 'a2')
		self.assertEqual(self.stack.pop(0), 'a1')
		self.assertEqual(self.stack.pop(1), 'b3')
		self.assertEqual(self.stack.pop(1), 'b2')
		self.assertEqual(self.stack.pop(1), 'b1')
		self.assertEqual(self.stack.pop(2), 'c3')
		self.assertEqual(self.stack.pop(2), 'c2')
		self.assertEqual(self.stack.pop(2), 'c1')

		print(n)

if __name__ == "__main__":
	unittest.main()