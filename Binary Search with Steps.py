def binary_search(arr,key):

    low=0
    high=len(arr)-1

    while low<=high:

        mid=(low+high)//2
        print("Mid index:",mid)

        if arr[mid]==key:
            return mid+1

        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1


arr=[3,9,14,19,25,31,42,47,53]

print("Position:",binary_search(arr,31))
