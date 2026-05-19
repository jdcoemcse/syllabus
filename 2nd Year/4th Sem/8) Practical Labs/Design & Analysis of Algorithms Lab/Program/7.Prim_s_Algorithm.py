import heapq

def prim_mst(g):
    n, v, h, c, e = len(g), [0]*len(g), [(0, 0, -1)], 0, []
    while h:
        w, u, p = heapq.heappop(h)
        if v[u]: continue
        v[u], c = 1, c + w
        if p != -1: e.append((p, u, w))
        for i in range(n):
            if g[u][i] and not v[i]:
                heapq.heappush(h, (g[u][i], i, u))
    return c, e

n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (use 0 for no edge):")
g = [list(map(int, input().split())) for _ in range(n)]

c, e = prim_mst(g)
print("\nMinimum Cost Spanning Tree (MST) Edges:")
for a, b, w in e: print(f"Edge ({a} - {b}) with weight {w}")
print("Total Minimum Cost of MST:", c)
