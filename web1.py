import urllib
from BeautifulSoup import*

url=raw_input("comments.txt")
html=urllib.urlopen(url).read()

soup=BeautifulSoup(html)

tags=soup('span')

numbers = []

for tag in tags:
    numbers.append(int(tag.string))

print sum(numbers)
