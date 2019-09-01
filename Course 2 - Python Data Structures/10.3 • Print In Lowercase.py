'''
file_prompt = raw_input("Write file name: ")  # 10-lower.txt
try:
    file = open(file_prompt)
except:
    print "Error in reading file."
    exit()
'''

name = raw_input("Input text: ")

content = name

# content = file.read()

output = content.strip()
output = content.lower()

print output