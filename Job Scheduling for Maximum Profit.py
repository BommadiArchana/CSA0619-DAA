import bisect

def jobScheduling(startTime,endTime,profit):
    jobs=sorted(zip(startTime,endTime,profit),key=lambda x:x[1])
    
    dp=[0]
    end=[0]
    
    for s,e,p in jobs:
        i=bisect.bisect(end,s)
        val=dp[i-1]+p
        
        if val>dp[-1]:
            dp.append(val)
            end.append(e)
    
    return dp[-1]

print(jobScheduling([1,2,3,3],[3,4,5,6],[50,10,40,70]))
print(jobScheduling([1,2,3,4,6],[3,5,10,6,9],[20,20,100,70,60]))
