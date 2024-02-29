# The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), 
# followed by a discussion. Enjoy!

# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. Hint: how does an even / odd number 
# react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.

num = int (input('Please enter a number: '))

if num % 4 == 0:
    print(f'The number {num} is an even number divisible by four. please handle with caution')
elif num % 2 == 0:
    print(f'The number {num} is an even number. please handle with caution')
else:
    print(f'The number {num} is an odd number. please handle with caution')


# Ask the user for two numbers: one number to check (call it num) and one 
# number to divide by (check). If check divides evenly into num, tell that to the user. 
# If not, print a different appropriate message.

num = int(input('Please enter a number: '))
dividend = int(input('Please enter a dividend: '))
def checkNum(num, dividend):   
    if num % dividend == 0:
        print(f'The number {num} is divisible by the dividend {dividend}')
    else:
        print(f'The number {num} is not divisible by the dividend {dividend}')

checkNum(num, dividend)