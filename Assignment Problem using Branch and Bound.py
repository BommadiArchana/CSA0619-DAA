cost = [
    [9,2,7],
    [6,4,3],
    [5,8,1]
]

N = 3
min_cost = float('inf')

def solve(worker, assigned, current_cost):
    global min_cost
    if worker == N:
        min_cost = min(min_cost, current_cost)
        return

    for job in range(N):
        if not assigned[job]:
            assigned[job] = True
            solve(worker+1, assigned, current_cost + cost[worker][job])
            assigned[job] = False

solve(0, [False]*N, 0)
print("Minimum Cost =", min_cost)
