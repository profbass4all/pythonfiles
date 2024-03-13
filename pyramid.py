num =int(input('Enter the height of your triangle: '))

for f in range(1, num+1):
    print((num-f) * ' ', end='')
    for x in range(f + (f-1)):
        if x%2 == 0:
            print('x', end='')
        else:
            print(' ', end='') 
    print('')