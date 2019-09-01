# Following Links in HTML Using BeautifulSoup

# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah

# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Macie.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: N

# To run this, download the BeautifulSoup `.zip` file: http://www.py4e.com/code3/bs4.zip and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' # sample
url = 'http://py4e-data.dr-chuck.net/known_by_Macie.html' # actual
# url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

hrefs = []
for link in soup.find_all('a'):
    href = link.get('href')
    hrefs.append(href)

# print(hrefs[2]) # Montgomery ✅
    
repeat = 1
input_repeat = input('Enter count: ')
input_repeat = int(input_repeat)
while repeat < input_repeat:
    # print('Repeat-Start:', repeat) # debug
    new_url = hrefs[17]
    new_html = urllib.request.urlopen(new_url, context=ctx).read()
    soup = BeautifulSoup(new_html, 'html.parser')
    hrefs.clear()
    hrefs = []
    for link in soup.find_all('a'):
        href = link.get('href')
        hrefs.append(href)
    print(hrefs[17])
    repeat = repeat + 1
    # print('Repeat-End:', repeat) # debug