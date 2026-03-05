graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

N = 4
path = [0]*N

def is_safe(v, pos):
    if graph[path[pos-1]][v] == 0:
        return False
    if v in path[:pos]:
        return False
    return True

def solve(pos):
    if pos == N:
        return graph[path[pos-1]][path[0]] == 1

    for v in range(1, N):
        if is_safe(v, pos):
            path[pos] = v
            if solve(pos+1):
                return True
            path[pos] = 0
    return False

if solve(1):
    print("Hamiltonian Cycle:", path+[path[0]])
else:
    print("No Hamiltonian Cycle")
