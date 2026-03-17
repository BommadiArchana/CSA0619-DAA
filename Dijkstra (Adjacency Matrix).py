import math

def dijkstra(graph,source):
    n=len(graph)
    dist=[math.inf]*n
    dist[source]=0
    visited=[False]*n
    
    for _ in range(n):
        u=min((d,i) for i,d in enumerate(dist) if not visited[i])[1]
        visited[u]=True
        
        for v in range(n):
            if graph[u][v]!=math.inf:
                dist[v]=min(dist[v],dist[u]+graph[u][v])
    
    return dist


graph=[
[0,10,3,math.inf,math.inf],
[math.inf,0,1,2,math.inf],
[math.inf,4,0,8,2],
[math.inf,math.inf,math.inf,0,7],
[math.inf,math.inf,math.inf,9,0]
]

print(dijkstra(graph,0))
