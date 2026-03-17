import heapq

def networkDelayTime(times,n,k):

    graph={i:[] for i in range(1,n+1)}

    for u,v,w in times:
        graph[u].append((v,w))

    pq=[(0,k)]
    dist={i:float('inf') for i in range(1,n+1)}
    dist[k]=0

    while pq:
        time,node=heapq.heappop(pq)

        for v,w in graph[node]:
            if time+w<dist[v]:
                dist[v]=time+w
                heapq.heappush(pq,(dist[v],v))

    ans=max(dist.values())

    return ans if ans<float('inf') else -1


print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
