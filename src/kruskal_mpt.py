import csv  
class MinimumSpanningTree:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.edges = []

    def add_connection(self, source, destination, weight):
        if source not in self.parent:
            self.parent[source] = source
            self.rank[source] = 0
        if destination not in self.parent:
            self.parent[destination] = destination
            self.rank[destination] = 0
        self.edges.append((source, destination, weight))

    def find_root(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find_root(self.parent[node])
        return self.parent[node]

    def merge_trees(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]: 
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1

    def get_connections(self):
        return self.edges   

    def all_nodes_connected(self):
        roots = set(self.find_root(node) for node in self.parent.keys())
        return len(roots) == 1


def find_min_cable_length(tree):
    connections = sorted(tree.get_connections(), key=lambda conn: conn[2])
    min_spanning_tree = []

    for connection in connections:
        node1, node2, weight = connection
        if tree.find_root(node1) != tree.find_root(node2):
            min_spanning_tree.append(connection)
            tree.merge_trees(node1, node2)

    total_length = sum(weight for _, _, weight in min_spanning_tree)
    return total_length if tree.all_nodes_connected() else -1


def read_csv(filename):
    mst = MinimumSpanningTree()
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if len(row) >= 3:
                source, destination, weight = row
                mst.add_connection(source, destination, int(weight))
            
    return mst


