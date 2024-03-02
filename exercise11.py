# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.)
num = int(input('Enter a number: '))

if num == 2 or num == 3 or num == 5:
    print('Its a prime number')
elif num == 1:
    print('It is not a prime number') 
elif num % 2 == 0:
    print('It is not a prime number')
elif num % 3 == 0:
    print('It is not a prime number')
elif num % 5 == 0:
    print('It is not a prime number')
else:
    print('It is a prime number')