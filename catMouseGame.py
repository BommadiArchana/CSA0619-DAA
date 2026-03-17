def catMouseGame(graph):
    mouse=1
    cat=2

    if 0 in graph[mouse]:
        return 1
    if mouse==cat:
        return 2

    return 0

print(catMouseGame([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]))
