# Ask the user what size game board they want to draw, and draw it for them to the 
# screen using Python’s print statement.
def boardGame():
    num = int(input('Enter the size of your board game:'))

    for i in range(num):
        print(' ---' * num)
        print('|   ' * (num+1))
    print(' ---' * num)

print(boardGame())