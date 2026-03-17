arr = [10, 7, 5, 18]
target = 25

def subset(sum_so_far, index):
    if sum_so_far == target:
        print("Subset found")
        return
    if index >= len(arr) or sum_so_far > target:
        return

    subset(sum_so_far + arr[index], index + 1)
    subset(sum_so_far, index + 1)

subset(0, 0)
