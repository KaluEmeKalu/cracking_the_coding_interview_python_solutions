import unittest
import random


class Node(object):
	def __init__(self, value, next_node=None):
		self.value = value
		self.next = next_node

	def partition(self, node):
		""" Run on root node """

		less_than = []
		greater_than_or_equal = []

		current = self
		while current:
			if current.value < node.value:
				less_than.append(current)
			else:
				greater_than_or_equal.append(current)
			current = current.next


		for i in range(len(less_than) -1):
			current = less_than[i]
			next_node = less_than[i+1]

			current.next = next_node

		current = next_node

		for i in range(len(greater_than_or_equal)):
			current.next = greater_than_or_equal[i]
			current = current.next

		current.next = None
		return self # self is root node


class testNode(unittest.TestCase):
	def testNode(self):
		a = Node(3)
		b = Node(5)
		c = Node(8)
		d = Node(5)
		e = Node(10)
		f = Node(10)
		g = Node(2)
		h = Node(1)

		a.next = b
		b.next = c
		c.next = d
		d.next = e
		e.next = f
		f.next = g
		g.next = h

		a.partition(d)

		current = a
		while current:
			print(current.value)
			current = current.next




if __name__ == "__main__":
	unittest.main()



