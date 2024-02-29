# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of 
# congratulations to the winner, and ask if the players want to start a new game)

win = False
while win == False:
    player1= input('Enter your play1: ').lower()
    player2= input('Enter your play2: ').lower()
    if player1 == player2:
        print('This is a draw')
    elif player1 == 'rock' and player2 == 'scissors':
        win = True
        print('Player 1 wins')
    elif player1 == 'scissors' and player2 == 'paper':
        win = True
        print('Player 1 wins')
    elif player1 == 'paper' and player2 == 'rock':
        win = True
        print('Player 1 wins')
    elif player2 == 'rock' and player1 == 'scissors':
        win = True
        print('Player 2 wins')
    elif player2 == 'scissors' and player1 == 'paper':
        win = True
        print('Player 2 wins')
    elif player2 == 'paper' and player1 == 'rock':
        win = True
        print('Player 2 wins')
    else:
        print('Enter a correct value for this game')
    
        
    
   


