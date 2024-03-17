tictactoe = [[2, 2, 1],
             [0, 2, 1],
             [2, 1, 2]
             ]
#column
for a in range(len(tictactoe)):
    if tictactoe[0][a] == tictactoe[1][a] == tictactoe[2][a] and tictactoe[0][a] != 0:
        print(f'Player {tictactoe[0][a]} won the game')
#row
for b in range(3):
    if len(set(tictactoe[b])) == 1 and tictactoe[b][0 != 0]:
        print(f'Player {tictactoe[b][0]} won the game')

#diagonal
if tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2] and tictactoe[0][0] != 0:
    print(f'Player {tictactoe[0][0]} won the game')
elif tictactoe[0][2] == tictactoe[1][1] == tictactoe[2][0] and tictactoe[0][2] != 0:
    print(f'Player {tictactoe[0][2]} won the game')

