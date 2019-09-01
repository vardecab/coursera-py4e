# 9.4 | Write a program to read through the mbox-short.txt [13-data.txt]
# and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.
# output: cwen@iupui.edu 5

file = open("13-data.txt")

list = list()  # ew. list = []
dictionary = dict()  # ew. dictionary = {}

for line in file:
    line = line.lower()
    line = line.strip()
    if line.startswith("from "):
        words = line.split()
        list.append(words[1])

for words in list:
    dictionary[words] = dictionary.get(words, 0) + 1

'''
max_value = max(dictionary.values())
max_key = [x for x, y in dictionary.items() if y == max_value]  # dunno what's goin' on

print max_key, max_value  # output with brackets
'''

key, value = max(dictionary.iteritems(), key=lambda x:x[1])  # output as desired // dunno what's goin' on

max_key = key
max_value = value

print max_key, max_value

# works here but not in autograder: max() arg is an empty sequence on line 17

# perfect solution

'''
fname = raw_input('Enter file name: ')

fhand = open(fname)

c = dict()

for line in fhand:
    if not line.startswith('From ') : continue
    pieces = line.split()
    email = pieces[1]
    c[email] = c.get(email,0) + 1

bigc = None
bige = None

for word in c:
    value = c[word]
    if bigc == None or value > bigc:
        bigw = word
        bigc = value

print bigw, bigc
'''