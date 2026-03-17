from itertools import permutations

graph=[
[0,10,15,20],
[10,0,35,25],
[15,35,0,30],
[20,25,30,0]
]

n=4
cities=list(range(1,n))

min_path=999999

for perm in permutations(cities):
    cost=0
    k=0
    for j in perm:
        cost+=graph[k][j]
        k=j
    cost+=graph[k][0]
    min_path=min(min_path,cost)

print("Minimum Path Distance:",min_path)
