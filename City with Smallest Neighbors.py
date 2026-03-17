INF=999

def findCity(n,edges,threshold):

    dist=[[INF]*n for _ in range(n)]

    for i in range(n):
        dist[i][i]=0

    for u,v,w in edges:
        dist[u][v]=w
        dist[v][u]=w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

    city=-1
    mincount=INF

    for i in range(n):
        count=sum(1 for j in range(n) if dist[i][j]<=threshold and i!=j)
        if count<=mincount:
            mincount=count
            city=i

    return city

print(findCity(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4))
