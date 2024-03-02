# Write a program that asks the user how many Fibonnaci numbers to generate and then 
# generates them. Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is 
#  the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
a = int(input('Enter the length of fib series: '))

b = [0, 1]
def fib(a):
    for i in range (a-2):
        c = b[-2] + b[-1]
        b.append(c)
    return b

print(fib(a))



