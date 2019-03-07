import unittest


class Node():
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __repr__(self):
        return f"{self.value}"


class Edge():
    def __init__(self, from_node, to_node, value=None):
        self.from_node = from_node
        self.to_node = to_node
        self.value = value

        # Add edge to From_node and To_node edges list
        from_node.edges.append(self)
        to_node.edges.append(self)


class Graph():
    def __init__(self):
        self.nodes = []
        self.edges = []

    def insert_node(self, value):
        node = Node(value)
        self.nodes.append(node)
        return node


    def get_or_create_node(self, node_val):
        for node in self.nodes:
            if node.value == node_val:
                return node

        # If node_val not found, create and return new node
        new_node = self.insert_node(node_val)
        return new_node



    def insert_edge(self, from_node_val, to_node_val, edge_value=None):
        from_node = self.get_or_create_node(from_node_val)
        to_node = self.get_or_create_node(to_node_val)

        edge = Edge(from_node, to_node, edge_value)
        self.edges.append(edge)
        return edge

    def get_edge_list(self):
        edge_set = []
        for edge in self.edges:
            tup = (edge.value, edge.from_node, edge.to_node)
            edge_set.append(tup)
        return edge_set

    def get_adjacency_dict(self):
        adjacency_dict = {}
        for edge in self.edges:
            info = (edge.to_node, edge.value)
            if edge.from_node in adjacency_dict:
                adjacency_dict[edge.from_node].append(info)
            else:
                adjacency_dict[edge.from_node] = [info]
        return adjacency_dict

    def get_max_vertex(self):
        the_max = self.nodes[0]
        for node in self.nodes:
            if node.value > the_max.value:
                the_max = node
        return the_max


    def get_adjacency_list(self):
        adjacency_list = [None] * (self.get_max_vertex().value + 1)
        for edge in self.edges:
            tup = (edge.value, edge.to_node.value)
            if adjacency_list[edge.from_node.value]:
                adjacency_list[edge.from_node.value].append(tup)
            else:  
                adjacency_list[edge.from_node.value] = [tup]
        return adjacency_list


    def get_node(self, node_value):
        for node in self.nodes:
            if node.value == node_value:
                return node
        raise ValueError(f"No Node with Value {node_value}")


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g = Graph()
        self.g.insert_edge(1, 2, 100)
        self.g.insert_edge(1, 3, 101)
        self.g.insert_edge(1, 4, 102)
        self.g.insert_edge(3, 4, 103)


    def testEdgeList(self):
        print(self.g.get_edge_list())

    def testGetAdjacencyDict(self):
        print(self.g.get_adjacency_dict())

    def testMax(self):
        node = self.g.get_node(4)
        self.assertEqual(self.g.get_max_vertex(), node)

    def testGetAdjacencyList(self):
        print(f"Here is adjacency list: {self.g.get_adjacency_list()}")


if __name__ == "__main__":
    unittest.main()
