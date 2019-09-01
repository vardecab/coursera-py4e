# 8.4 | Open the file romeo.txt [11-data.txt] and read it line by line.
# For each line, split the line into a list of words using the split() function.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words [11-output.txt] in alphabetical order.
# You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

file = open("11-data.txt")

vault = list()

for line in file:
    line = line.split()
    for word in line:
        if word not in vault:
            vault.append(word)

vault.sort()
print vault