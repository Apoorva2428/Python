str1 = "This is a string"
print(str1[0])
print(str1[0:7]) #0 including but 7 excluding
print(str1[0:6])

#length function
print(len(str1)) #0 to 15

#skipping characters
print(str1[0:6:2])

#by default taking the gap is 1 and by default starting is 0 and by default ending is infinity
print(str1[::])
print(str1[:5:2])
print(str1[0:])
print(str1[0:12])

#Negative indices
print(str1[-4:-2])

#Putting - in third one; it wil reverse the string
print(str1[::-1])

#String functions check documentation on google