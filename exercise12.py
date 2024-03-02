# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. For practice, 
# write this code inside a function

a = []
b  = int(input('Enter a length for your list: '))
for x in range(b):
    d = int(input('Enter a number: '))
    a.append(d)

def isList(a):
    return [a[0], a[-1]]

print(isList(a))


