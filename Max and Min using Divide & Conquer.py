def max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        return (min(arr[low], arr[high]),
                max(arr[low], arr[high]))

    mid = (low + high) // 2
    min1, max1 = max_min(arr, low, mid)
    min2, max2 = max_min(arr, mid+1, high)

    return min(min1, min2), max(max1, max2)

arr = [7, 2, 9, 4, 1]
minimum, maximum = max_min(arr, 0, len(arr)-1)

print("Minimum:", minimum)
print("Maximum:", maximum)
