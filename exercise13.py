# Write a program that asks the user how many Fibonnaci numbers to generate and then 
# generates them. Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is 
#  the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def isFib():
    a = int(input('Enter the length of fib series: '))

    if a == 0:
        fib =[]
    elif a ==1:
        fib =[0]
    elif a ==2:
        fib =[0, 1]
    elif a > 2:
        fib = [0,1]
        for d in range(a-2):
            g = fib[d] + fib[-1]
            fib.append(g)
    return fib

print(isFib())



