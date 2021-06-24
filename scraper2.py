from bs4 import BeautifulSoup
html_text=open('basic.html')
soup=BeautifulSoup(html_text,'html.parser')
h1_scrape=soup.find_all('h1')
for tag in h1_scrape:
    print(tag.text)