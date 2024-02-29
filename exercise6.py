# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

name = input('Please enter a string: ')
def isPalindrome(palin):
    x = len(palin)
    y = x // 2

    q = palin[0:y + 1]
    s = palin[-(y + 1):][::-1]
    if q == s:
        print('The word is a palindrome')
    else:
        print('The word is not a palindrome')



isPalindrome(name)
