import heapq

def kClosest(points,k):

    points.sort(key=lambda p: p[0]**2+p[1]**2)

    return points[:k]


points=[[1,3],[-2,2],[5,8],[0,1]]

print(kClosest(points,2))
