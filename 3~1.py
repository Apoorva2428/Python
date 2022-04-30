"""def linear_search(arr, key):
    for (ind, value) in enumerate(arr):
        if key == value:
            return ind
    return None

inp = [int(num) for num in input('Enter a list of integers(space-seperated) : ').strip().split()]
keyNum = int(input('Enter the number you want to search for : '))
index = linear_search(inp, keyNum)
if index != None:
    print(f'{keyNum} Item present at index {index}.')
else:
    print(f'{keyNum} Item not present in the array.')"""

"""def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


inp = [int(num) for num in input('Enter a list of integers(space-seperated) : ').strip().split()]
bubble_sort(inp)
print(f'After sorting the array is : {inp}')"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]

inp = [int(num) for num in input('Enter a list of integers(space-seperated) : ').strip().split()]
selection_sort(inp)
print(f'After sorting the array is : {inp}')
