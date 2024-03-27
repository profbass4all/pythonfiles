a = [
    ['0','0','0'], 
    ['0','0','0'],
    ['0','0','0']
    ]
num = 0
count = 0

while count <= 9:
    b = input('Enter a position player 1: ').strip()
    count +=1
    d = b.split(',')
    f = int(d[0])
    g = int(d[1])
    if '#' != a[f][g] and 'X' != a[f][g]:
        a[f][g] = '#'
    else:
        print('The spot has been filled, enter a new position')
        b = input('Enter a position player 1: ').strip()

    for row in a:
        print(row)

    c = input('Enter a position player 2: ').strip()
    e = c.split(',')
    h = int(e[0])
    i = int(e[1])
    if '#' != a[h][i] and 'X' != a[h][i]:
        a[h][i] = 'X'
    else:
        print('The spot has been filled, enter a new position')
        c = input('Enter a position player 2: ').strip()

    for row in a:
        print(row)

    
count+=1


