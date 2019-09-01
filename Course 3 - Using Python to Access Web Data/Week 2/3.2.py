# Extracting Data With Regular Expressions

# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re
# import os

file_name = 'regex_sum_162621.txt'

with open(file_name) as sample_data_file:  
    read_file = sample_data_file.read() 

search = re.findall('[0-9]+', read_file)
print (search) # check what's inside
results = list(map(int, search)) # convert to int
print (sum(results))

# print (os.listdir()) # list all files in dic
# print (os.getcwd()) # get location
