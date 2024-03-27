import random

def randomWord():
    with open('sowpods.txt', 'r') as f:
        line = f.readlines()
        word = random.choice(line).strip()
        return word


a = randomWord() 
print(a)
def makeGuess(a):
    
    d = []
    for x in range(len(a)):
        d.append('_')
    h = ''
    num =0
    loose = 0
    while a!= h:
        b = input('Enter a letter: ').upper().strip()
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
            print(f'Your incorrect guesses remains just {6-loose} ')
            if loose == 6:
                print(f'Your {loose} trials are all used up')
                break

    if a == h:
        print(f'Congratulations!! \nYou got the word in {num} trials' )

makeGuess(a)
