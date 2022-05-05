"""d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

def add_dict(d1, d2):
    new_dict = {}
    for key in d1:
        if key in d2:
            new_dict[key] = d1[key] + d2[key]
        else:
            new_dict[key] = d1[key]
    for key in d2:
        if key not in d1:
            new_dict[key] = d2[key]
    return new_dict

print('First dictionary is : ', d1)
print('Second dictionary is : ', d2)
print('Their sum is : ', add_dict(d1, d2))"""

def get_values():
    inp = input('Enter key and value (space-seperated) : ').strip().split()
    return tuple(int(num) for num in inp)
n = int(input('Enter the size of the dictionary : '))
d = {}
for _ in range(n):
    inp = get_values()
    d[inp[0]] = inp[1]
keys = list(d.keys())
keys.sort(reverse=True)
print('The dicitonary is :', d)
print('Highest 3 values of keys in dictionary are : ', keys[:3])
