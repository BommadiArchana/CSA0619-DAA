def median_of_medians(arr,k):

    arr.sort()

    return arr[k-1]


print(median_of_medians([1,2,3,4,5,6,7,8,9,10],6))
