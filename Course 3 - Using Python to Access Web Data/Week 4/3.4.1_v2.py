# Scraping Numbers from HTML using BeautifulSoup

# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_162623.html (Sum ends with 81)

# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# url = 'http://py4e-data.dr-chuck.net/comments_42.html' # sample
url = 'http://py4e-data.dr-chuck.net/comments_162623.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

numbers = []

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)

    number = tag.contents[0]
    numbers.append(number)

# print(numbers) # debug ✅

results = list(map(int, numbers))
# print(results) # debug ✅

print(sum(results))