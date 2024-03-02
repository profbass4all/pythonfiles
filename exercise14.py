# Write a program (function!) that takes a list and returns a new list that 
# contains all the elements of the first list minus all the duplicates.

a = [2,3,4,2,2,3,3,4,4,5,6,89,54,21,56,56,56,5,5,5]

def isduplicate(a):
    b = []
    for x in a:
        if x in b:
            continue
        else:
            b.append(x)
    return b

print(isduplicate(a))
#or
print(set(a))

