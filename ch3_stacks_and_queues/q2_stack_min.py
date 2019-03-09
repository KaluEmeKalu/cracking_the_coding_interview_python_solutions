import unittest

class Node(object):
	def __init__(self, value):
		self.value = value
		self.min_before = None

class StackMin(object):
	def __init__(self):
		self._array = []
		self.min = None

	def get_min(self):
		return self.min.value


	def push(self, val):
		node = Node(val)
		self._array.append(node)

		node.min_before = self.min

		if self.min:
			if node.value <= self.min.value:
				self.min = node
		else:
			self.min = node

	def pop(self):
		item = self._array.pop()

		if item == self.min:
			self.min = item.min_before
		return item.value


class TestStackMin(unittest.TestCase):
	def test_min(self):
		s = StackMin()
		s.push(4)

		self.assertEqual(s.get_min(), 4)

		s.push(6)
		self.assertEqual(s.get_min(), 4)
		s.push(2)
		self.assertEqual(s.get_min(), 2)
		s.push(10)
		self.assertEqual(s.get_min(), 2)

		s.pop()
		self.assertEqual(s.get_min(), 2)

		s.pop()
		self.assertEqual(s.get_min(), 4)




if __name__ == "__main__":
	unittest.main()