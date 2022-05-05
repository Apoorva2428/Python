"""def last(n): 
    return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)

print(sort_list_last([(7, 9), (3, 5), (2, 4), (1, 2), (2, 1)]))
"""
colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour = [x for (i,x) in enumerate(colour) if i not in (0,4,5)]
print(colour)
