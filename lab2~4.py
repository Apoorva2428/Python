"""inp = input('Enter the values in tuple (space-seperated) : ').strip().split()
inp = tuple(int(num) for num in inp)
num = int(input('Enter the new value of the last element : '))

print('The original tuple is', inp)
print('The new tuple with last value replaced is :', inp[:-1]+(num,))
"""

def get_tuple():
    inp = input('Enter the values in tuple (space-seperated) : ').strip().split()
    inp = tuple(int(num) for num in inp)
    return inp
n = int(input('Enter the number of tuples in the list : '))
lst = []
for _ in range(n):
    lst.append(get_tuple())
print('The original list is', lst)
new_lst = [tup for tup in lst if tup]
print('The new list with non-empty tuples is  :', new_lst)
