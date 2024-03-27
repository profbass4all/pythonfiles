# Implement a function that takes as input three variables, and returns the largest of the three. 
# Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally takes 
# care of for us. All you need is some variables and if statements!

maxofThree = input('Enter the three numbers: ')
num = maxofThree.strip().split(',')
firstNum = int(num[0].strip())
secondNum = int(num[1].strip())
thirdNum = int(num[2].strip())
nums = [firstNum, secondNum, thirdNum]
greatest = 0

for x in nums:
    if x >= greatest:
        greatest = x
print(greatest)