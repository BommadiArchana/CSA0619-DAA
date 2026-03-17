def kth_smallest(arr,k):

    arr.sort()

    return arr[k-1]


arr=[12,3,5,7,19]

print(kth_smallest(arr,2))
