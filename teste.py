from bs4 import BeautifulSoup

data='<span class="rating-count">TEXT I WANT</span>'
soup=BeautifulSoup(data)
t=soup.find('span',{'class':'rating-count'})
print (t.text)