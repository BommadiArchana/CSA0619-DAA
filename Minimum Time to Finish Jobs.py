def minimumTimeRequired(jobs,k):
    workers=[0]*k
    
    jobs.sort(reverse=True)
    
    def backtrack(i):
        if i==len(jobs):
            return max(workers)
        
        res=float('inf')
        
        for j in range(k):
            workers[j]+=jobs[i]
            res=min(res,backtrack(i+1))
            workers[j]-=jobs[i]
            
            if workers[j]==0:
                break
        
        return res
    
    return backtrack(0)

print(minimumTimeRequired([3,2,3],3))
print(minimumTimeRequired([1,2,4,7,8],2))
