# For this exercise, write the logic that asks a player to guess a letter and 
# displays letters in the clue word that were guessed correctly. For now, let 
# the player guess an infinite number of times until they get the entire word. 
# As a bonus, keep track of the letters the player guessed and display a different 
# message if the player tries to guess that letter again. Remember to stop the game 
# when all the letters have been guessed correctly!
a = 'evaporate'
d = []
for x in range(len(a)):
    d.append('_')
h = ''
num =0
loose = 0
while a!= h:
    b = input('Enter a letter: ').lower().strip()
    num += 1
    if b in a:
        if b in set(d):
            print('You\'ve guessed this before')
            continue
        for x in range(len(a)):
            if a[x] == b:
                d[x] = b 
        h = ''.join(d)
        print(h)
    else:
        print('Incorrect Letter')
        loose += 1
        if loose == 2:
            print(f'Your {loose} trials are all used up')
            break

if a == h:
    print(f'Congratulations!! \nYou got the word in {num} trials' )
