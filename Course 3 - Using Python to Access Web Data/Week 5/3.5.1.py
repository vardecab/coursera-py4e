# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_162625.xml (Sum ends with 50)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_162625.xml'
# url = input('Enter location: ')
print('Retrieving: ', url)

page = urllib.request.urlopen(url)
read_page = page.read()

print('Retrieved', len(read_page), 'characters.')

# print(read_page) # raw output

# data_decoded = read_page.decode() # nicely looking XML
# print(data_decoded) # nicely looking XML

tree = ET.fromstring(read_page)
comments = tree.find('comments').findall('comment')

sum = 0

for comment in comments:
    count = comment.find('count').text
    count = int(count)
    sum += count

print(comments)
print('Count:', len(comments))
print('Sum:', sum)