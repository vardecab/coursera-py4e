# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_162626.json (Sum ends with 61)

import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_42.json' # sample
# url = 'http://py4e-data.dr-chuck.net/comments_162626.json' # actual
# url = input('Enter location: ')

print('Retrieving: ', url)

page = urllib.request.urlopen(url)
read_page = page.read().decode()

print('Retrieved', len(read_page), 'characters.')

print(read_page) # debug ✅