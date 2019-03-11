import unittest

class Node(object):
	def __init__(self, value, next_node=None):
		self.value = value
		self.next = next_node
		self.index = None


	def remove_kth_to_last(self, kth, index_to_delete=None):
		"""Can only be called from root"""
		prev = self
		prev.index = 1
		current = self.next
		while current:
			if index_to_delete and index_to_delete == current.index: # base case
				prev.next = current.next
				return current

			current.index = prev.index + 1
			prev = current
			current = current.next


		index_to_delete = prev.index - kth + 1
		if kth == prev.index:
			return self
		return self.remove_kth_to_last(kth, index_to_delete)


class TestNode(unittest.TestCase):
	def setUp(self):
		self.root = Node('A')
		self.b = Node('B')
		self.c = Node('C')
		self.d = Node('D')
		self.e = Node('E')
		self.root.next = self.b
		self.b.next = self.c
		self.c.next = self.d
		self.d.next = self.e

	def test_remove_kth(self):
		self.assertEqual(self.root.remove_kth_to_last(1), self.e)
	def test_remove_kth_again(self):
		self.assertEqual(self.root.remove_kth_to_last(5), self.root)

if __name__ == "__main__":
	unittest.main()
