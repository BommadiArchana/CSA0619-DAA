INF = 999

n = 5
dist = [[INF]*n for _ in range(n)]

edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]

for i in range(n):
    dist[i][i] = 0

for u,v,w in edges:
    dist[u][v] = w
    dist[v][u] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

threshold = 2
city = -1
min_count = INF

for i in range(n):
    count = sum(1 for j in range(n) if dist[i][j] <= threshold and i!=j)
    if count <= min_count:
        min_count = count
        city = i

print("City:", city)
