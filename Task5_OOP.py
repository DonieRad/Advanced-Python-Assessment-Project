# TASK 5 #

from collections import defaultdict

# define the weighted graph class
class Weight_graph:
    def __init__(self):
        self.vertices = set()  # stores all vertices in the graph
        self.edges = defaultdict(list)  # stores adjacency list (edges)
        self.weights = {}  # stores edge weights as (v, u): weight

    # add a vertex to the graph
    def add_vertex(self, v):
        self.vertices.add(v)

    # sdd an edge between vertex v and vertex u with a given distance (weight)
    def add_edge(self, v, u, dist):
        self.edges[v].append(u)
        self.weights[(v, u)] = dist

    # method to compute and print the average of weights attached to a vertex
    def average_edge_weight(self, vertex):
        # get all outgoing edges from the vertex
        connected_vertices = self.edges[vertex]
        if not connected_vertices:
            print(f"No edges attached to vertex '{vertex}'")
            return

        # sum all the weights for edges starting from this vertex
        total_weight = 0
        for u in connected_vertices:
            total_weight += self.weights[(vertex, u)]
            # calculate and print average
            average = total_weight / len(connected_vertices)
            print(f"Average weight for edges from vertex '{vertex}': {average}")

    # dunder method to modify behavior of the power operator (**)
    def __pow__(self, power):
        # raise each weight in the graph to the given power
        for key in self.weights:
            self.weights[key] = self.weights[key] ** power

# create the graph using the class above
g = Weight_graph()

# add vertices
for v in ['X', 'Y', 'Z', 'W', 'V']:
    g.add_vertex(v)

# add edges
g.add_edge('X', 'Y', 4)
g.add_edge('X', 'Z', 2)
g.add_edge('Y', 'Z', 5)
g.add_edge('Y', 'W', 10)
g.add_edge('Z', 'W', 3)
g.add_edge('W', 'V', 8)


# test average edge weight from some vertices
g.average_edge_weight('X')
g.average_edge_weight('Y')
g.average_edge_weight('W')

# raise all weights to the power of 2
g ** 2

# print weights to confirm they’ve been updated
print('Updated weights after power of 2:')
for edge, weight in g.weights.items():
    print(f'{edge}: {weight}')