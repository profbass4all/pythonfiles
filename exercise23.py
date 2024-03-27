# In this exercise, the task is to write a function that picks a random word
# from a list of words from the SOWPODS dictionary

import random

def randomWord():
    with open('sowpods.txt', 'r') as f:
        line = f.readlines()

        word = random.choice(line)
        return(word)

print(randomWord())
