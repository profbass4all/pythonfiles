# Given a .txt file that has a list of a bunch of names, count how many of each name there are 
# in the file, and print out the results to the screen

names = {}
with open('names.txt', 'r') as read_file:
    
    line = read_file.readline()
    while line:
        line = line.strip()
        if line in names:
            names[line] += 1
        else:
            names[line] = 1
        line = read_file.readline()
print(names)


