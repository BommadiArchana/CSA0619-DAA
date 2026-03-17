def fourSumCount(A,B,C,D):

    count=0

    for a in A:
        for b in B:
            for c in C:
                for d in D:
                    if a+b+c+d==0:
                        count+=1

    return count


A=[1,2]
B=[-2,-1]
C=[-1,2]
D=[0,2]

print(fourSumCount(A,B,C,D))
