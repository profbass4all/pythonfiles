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
