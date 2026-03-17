from itertools import combinations

def closest_sum(arr,target):

    best=0

    for r in range(len(arr)+1):
        for comb in combinations(arr,r):
            s=sum(comb)
            if abs(target-s) < abs(target-best):
                best=s

    return best


arr=[45,34,4,12,5,2]

print(closest_sum(arr,42))
