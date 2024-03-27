with open('abc.txt', 'a') as fileA:
    fileA.write('\nZeeky is lovely')

try:
    a = int(input('Enter your age: '))
except (ZeroDivisionError, ValueError):
    print('please enter a name')
else:
    print(a)
finally:
    print('good boy')

