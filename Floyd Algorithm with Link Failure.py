INF = 999

dist = [
[0,1,5,INF,INF,INF],
[1,0,2,1,INF,INF],
[5,2,0,INF,3,INF],
[INF,1,INF,0,1,6],
[INF,INF,3,1,0,2],
[INF,INF,INF,6,2,0]
]

n = 6

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print("Shortest path A to F:", dist[0][5])
