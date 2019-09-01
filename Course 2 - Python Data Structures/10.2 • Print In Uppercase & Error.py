# 7.1 | Write a program that prompts for a file name
# then opens that file and reads through the file
# and print the contents of the file in upper case.
# Use the file words.txt [10-data.txt] to produce the output below:
# // desired output is in 10-output.txt file
# You can download the sample data at http://www.pythonlearn.com/code/words.txt

file_prompt = raw_input("Write file name: ")  # 10-data.txt
try:
    file = open(file_prompt)
except:
    print "Error in reading file."
    exit()

content = file.read()

output = content.strip()
output = content.upper()

print output