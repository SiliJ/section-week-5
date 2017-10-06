import requests
from bs4 import BeautifulSoup
try:
  nytimes= open("NYT.html",'r').read()
except:
  nytimes = requests.get("http://www.nytimes.com/pages/todayspaper/index.html").text
  f = open("NYT.html",'w')
  f.write(nytimes) # more in the chapter on Files in textbook
  f.close()
