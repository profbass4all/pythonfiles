# Write a function that takes an ordered list of numbers (a list where the elements 
# are in order from smallest to largest) and another number. The function decides 
# whether or not the given number is inside the list and returns (then prints) 
# an appropriate boolean

a = [2,5,8,9,40]
num = int(input('Enter a number: '))
c = a.__contains__(num)
print(c)