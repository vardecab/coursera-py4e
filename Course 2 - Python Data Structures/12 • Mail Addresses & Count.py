# 8.5 | Open the file mbox-short.txt [12-data.txt] and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line
# (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

file = open("12-data.txt")

vault = list()  # ew. vault = []
count = 0

for line in file:
    line = line.strip()
    line = line.lower()
    if line.startswith("from "):
        count = count + 1

        words = line.split()
        output = words[1]
        
        print (output)

print ("There were", count, "lines in the file with From as the first word")
