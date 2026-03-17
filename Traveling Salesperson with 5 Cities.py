from itertools import permutations

cities=['A','B','C','D','E']

dist={
('A','B'):10,('A','C'):15,('A','D'):20,('A','E'):25,
('B','C'):35,('B','D'):25,('B','E'):30,
('C','D'):30,('C','E'):20,
('D','E'):15
}

def get(a,b):
    if (a,b) in dist:
        return dist[(a,b)]
    return dist[(b,a)]

start='A'
others=[c for c in cities if c!=start]

min_cost=99999

for perm in permutations(others):
    route=[start]+list(perm)+[start]
    cost=0
    for i in range(len(route)-1):
        cost+=get(route[i],route[i+1])
    min_cost=min(min_cost,cost)

print("Minimum Distance:",min_cost)
