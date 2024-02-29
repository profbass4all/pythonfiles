# write a program that returns a list that contains only 
# the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes without using sets

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [x for x in a if x in b]

d = []
for x in c:
    if x not in d:
        d.append(x)
    else:
        continue
    
print(d)