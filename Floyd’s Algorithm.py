INF = 9999

graph = [
    [0,5,INF,10],
    [INF,0,3,INF],
    [INF,INF,0,1],
    [INF,INF,INF,0]
]

n = 4

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print("Shortest Path Matrix:")
for row in graph:
    print(row)
