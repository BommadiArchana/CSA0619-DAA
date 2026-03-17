INF = 999

graph = [
[0,3,INF,INF],
[INF,0,1,4],
[INF,INF,0,1],
[INF,INF,INF,0]
]

n = 4

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in graph:
    print(row)
