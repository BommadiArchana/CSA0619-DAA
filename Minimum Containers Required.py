def minContainers(weights,capacity):
    
    weights.sort(reverse=True)
    containers=0
    
    while weights:
        space=capacity
        
        for w in weights[:]:
            if w<=space:
                space-=w
                weights.remove(w)
        
        containers+=1
    
    return containers

print(minContainers([5,10,15,20,25,30,35],50))
print(minContainers([10,20,30,40,50,60,70,80],100))
