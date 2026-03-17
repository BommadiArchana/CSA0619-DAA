import heapq

def maxProbability(n, edges, prob, start, end):
    graph={i:[] for i in range(n)}

    for (u,v),p in zip(edges,prob):
        graph[u].append((v,p))
        graph[v].append((u,p))

    pq=[(-1,start)]
    dist=[0]*n
    dist[start]=1

    while pq:
        pr,node=heapq.heappop(pq)
        pr=-pr

        if node==end:
            return pr

        for nei,p in graph[node]:
            if pr*p>dist[nei]:
                dist[nei]=pr*p
                heapq.heappush(pq,(-dist[nei],nei))

    return 0

print(maxProbability(3,[[0,1],[1,2],[0,2]],[0.5,0.5,0.2],0,2))
