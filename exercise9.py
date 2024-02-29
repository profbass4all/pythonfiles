# Generate a random number between 1 and 9 
# (including 1 and 9). Ask the user to guess the number, 
# then tell them whether they guessed too low, too high, or exactly right.
import random

randNum = random.randint(1,9)
isCorrect = False
count = 0
while isCorrect == False:
    num = int(input('Enter your number: '))
    
    count += 1
    if(num < randNum):
        print(f'{int(num)} is less than the number. keep trying babe')
        isCorrect = False
    elif(num > randNum):
        print(f'{num} is too high than the number you\'re searching for, keep trying babe')
        isCorrect = False
    elif(num == randNum):
        print(f'finally! you got the number after you\'ve tried {count} times...congratulations')
        isCorrect = True
        if isCorrect:
            break
    else:
        print(f'type a correct number')
    check = input('Do you wanna exit? ')
    if check == 'yes':
        print('I exit')
        break
        
    
    


