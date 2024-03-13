# Given two .txt files that have lists of numbers in them, 
# find the numbers that are overlapping. One .txt file has a list of all 
# prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000

prime = []
happy = []

with open('primeNo.txt', 'r') as primenum:
    line = primenum.readline()
    while line:
        line = line.strip()
        prime.append(line)
        line = primenum.readline()
with open('happyNo.txt', 'r') as happynum:
    line = happynum.readline()
    while line:
        line = line.strip()
        happy.append(line)
        line = happynum.readline()
overlap = []
for a in prime:
    if a in happy:
        overlap.append(a)
    else:
        continue
print(overlap)
