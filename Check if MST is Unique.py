# Kruskal Algorithm
def kruskal(n, edges):

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    edges = sorted(edges, key=lambda x: x[2])

    mst = []
    total = 0

    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
            total += w

    return mst, total


def mst_unique(n, edges, given_mst):

    mst, total = kruskal(n, edges)

    if set(mst) == set(given_mst):
        print("Is the given MST unique? True")
    else:
        print("Is the given MST unique? False")
        print("Another possible MST:", mst)
        print("Total weight of MST:", total)


edges = [(0,1,1),(0,2,1),(1,3,2),(2,3,2),(3,4,3),(4,2,3)]

given = [(0,1,1),(0,2,1),(1,3,2),(3,4,3)]

mst_unique(5, edges, given)
