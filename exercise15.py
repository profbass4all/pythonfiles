# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. 
                 
def backwardstring():
    a = input('Enter a string: ')
    b = a.split()
    d = b[::-1]
    c =' '.join(d)
    return c

print(backwardstring())