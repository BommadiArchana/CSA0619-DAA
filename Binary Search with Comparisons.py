def binary_search(arr,key):

    low=0
    high=len(arr)-1
    count=0

    while low<=high:
        mid=(low+high)//2
        count+=1

        if arr[mid]==key:
            return mid+1,count

        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1

    return -1,count


arr=[5,10,15,20,25,30,35,40,45]

pos,c=binary_search(arr,20)

print("Position:",pos)
print("Comparisons:",c)
