import heapq

def dijkstra_edge(n,edges,source,target):
    
    graph={i:[] for i in range(n)}
    
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    pq=[(0,source)]
    dist=[float('inf')]*n
    dist[source]=0
    
    while pq:
        d,u=heapq.heappop(pq)
        
        if u==target:
            return d
        
        for v,w in graph[u]:
            if d+w<dist[v]:
                dist[v]=d+w
                heapq.heappush(pq,(dist[v],v))
    
    return dist[target]

edges=[(0,1,7),(0,2,9),(0,5,14),(1,2,10),(1,3,15),(2,3,11),(2,5,2),(3,4,6),(4,5,9)]

print(dijkstra_edge(6,edges,0,4))
