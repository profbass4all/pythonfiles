# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# For every digit the user guessed correctly in the wrong place is a “bull.” 
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# Once the user guesses the correct number, the game is over. Keep track of the number of 
# guesses the user makes throughout teh game and tell the user at the end.

import random
rand = str(random.randint(1000,9999))

def guessGame():
    success = False
    count =0
    while success == False:
        cow, bull = 0, 0
        user = input('Enter your guess: ')
        count +=1
        if user == rand:
                print('You guessed right')
                success = True
                break
        for x in range(4):
            if user[x] == rand[x]:
                cow += 1
            elif user[x] in rand:
                 bull +=1
            
        print(f'{cow} cow {bull} bull')
    print(f'you guessed {count} times')
guessGame()
