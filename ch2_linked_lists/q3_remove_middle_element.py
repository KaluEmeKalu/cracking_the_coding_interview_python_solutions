import unittest

class Node(object):
	def __init__(self, value, next_node=None):
		self.value = value
		self.next = next_node

	@staticmethod
	def remove_middle_element(middle_element):
		"""Must run from root"""

		middle_element.value = middle_element.next.value
		middle_element.next = middle_element.next.next


	def get_node_or_none(self, value, root=None):
		""" Returns node if node exists
		Else returns None
		"""
		current = root if root else self

		while current:
			if current.value == value:
				return current
			current = current.next
		return current


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

	def test_remove_middle(self):
		Node.remove_middle_element(self.d)

		self.assertEqual(None, self.root.get_node_or_none(self.d))

if __name__ == "__main__":
	unittest.main()