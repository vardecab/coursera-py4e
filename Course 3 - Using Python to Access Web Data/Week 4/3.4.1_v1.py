# You are to find all the <span> tags in the file (http://py4e-data.dr-chuck.net/comments_162623.html) and pull out the numbers from the tag and sum the numbers.

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_162623.html'
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

elements = list()

tags = soup('span')
for tag in tags:
    elements.append(tag.contents[0])
 
numbers = list(map(int, elements))
print (sum(numbers))