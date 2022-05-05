def linear_search(arr, n):
   for i in range(len(arr)):
      if arr[i] == n:
         return i
   return -1
arr = [1, 2, 7, 24, 55, 70]
n = 2
r = linear_search(arr, n)
if(r == -1):
    print("Not found")
else: 
    print(str(r))