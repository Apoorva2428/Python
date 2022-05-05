def binary_search(arr, n):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else: 
            return mid
    return -1
arr = [1, 2, 7, 14, 24, 56]
n = 7
r = binary_search(arr, n)
if r != -1:
    print(str(r))
else: 
    print("Not found")