def greedyLoad(weights,capacity):
    
    weights.sort(reverse=True)
    total=0
    
    for w in weights:
        if total+w<=capacity:
            total+=w
    
    return total

print(greedyLoad([10,20,30,40,50],60))
print(greedyLoad([5,10,15,20,25,30],50))
