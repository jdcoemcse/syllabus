class Graph:
    def __init__(self, vertices):
        self.V, self.edges = vertices, []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find_parent(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find_parent(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x, root_y = self.find_parent(parent, x), self.find_parent(parent, y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
                rank[root_y] += rank[root_x] == rank[root_y]

    def kruskal_mst(self):
        self.edges.sort()
        parent, rank, mst = list(range(self.V)), [0] * self.V, []
        for weight, u, v in self.edges:
            if (root_u := self.find_parent(parent, u)) != (root_v := self.find_parent(parent, v)):
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)
                if len(mst) == self.V - 1: break
        print("Edges in MST:", *[f"{u} -- {v} == {w}" for u, v, w in mst], sep="\n")
        print("Minimum Cost:", sum(w for _, _, w in mst))

V = int(input("Enter number of vertices: "))
g = Graph(V)

print("Enter adjacency matrix (use 0 for no edge):")
for i in range(V):
    for j, w in enumerate(map(int, input().split())):
        if i < j and w: g.add_edge(i, j, w)

g.kruskal_mst()
