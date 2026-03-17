def mst_unique(n,edges,given_mst):
    
    mst,total=kruskal(n,edges)
    
    if set(mst)==set(given_mst):
        print("Is the given MST unique? True")
    else:
        print("Is the given MST unique? False")
        print("Another possible MST:",mst)

edges=[(0,1,1),(0,2,1),(1,3,2),(2,3,2),(3,4,3),(4,2,3)]

given=[(0,1,1),(0,2,1),(1,3,2),(3,4,3)]

mst_unique(5,edges,given)
