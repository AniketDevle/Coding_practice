import requests
from bs4 import BeautifulSoup

Search_words = "Mobile Phones"
words = Search_words.split()
Str = words[0]
for i in words[1:]:
    Str = Str + "+" + i

website = "https://www.amazon.com/s?k="

URL = website + Str

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}



Page = requests.get(URL , headers = headers)

soup = BeautifulSoup(Page.text, 'xml')

b = soup.find_all('div' , attrs= {'class' : 'sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 sg-col-4-of-28 s-matching-dir sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32'})

print(len(b))

for d in soup.find_all('div', attrs={'class': 'sg-col-20-of-24 s-matching-dir sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-8-of-12 sg-col-12-of-16 sg-col-24-of-28'}):
    name = d.findAll('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})[0].text
    price = d.findAll('span', attrs={'class': 'a-offscreen'})[0].text
    rating = d.findAll('span', attrs={'class': 'a-icon-alt'})[0].text

    print(name)
