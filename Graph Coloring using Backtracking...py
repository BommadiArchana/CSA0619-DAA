graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

N = 4
color = [0]*N

def is_safe(v, c):
    for i in range(N):
        if graph[v][i] and color[i] == c:
            return False
    return True

def solve(v):
    if v == N:
        print("Coloring:", color)
        return True

    for c in range(1, 4):
        if is_safe(v, c):
            color[v] = c
            if solve(v+1):
                return True
            color[v] = 0
    return False

solve(0)
