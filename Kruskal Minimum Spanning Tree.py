def kruskal(n,edges):
    
    parent=list(range(n))
    
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    
    def union(x,y):
        parent[find(x)]=find(y)
    
    edges.sort(key=lambda x:x[2])
    
    mst=[]
    total=0
    
    for u,v,w in edges:
        if find(u)!=find(v):
            union(u,v)
            mst.append((u,v,w))
            total+=w
    
    return mst,total


edges=[(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]

print(kruskal(4,edges))
