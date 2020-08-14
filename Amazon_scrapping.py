import requests
from bs4 import BeautifulSoup
import pandas as pd

Search_words = "Mobile Phones"
words = Search_words.split()
Str = words[0]
for i in words[1:]:
    Str = Str + "+" + i

website = "https://www.amazon.com/s?k="

URL = website + Str

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Pixel 2 XL Build/OPM1.171019.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8", "DNT": "1",
    "Connection": "close", "Upgrade-Insecure-Requests": "1"
}

page = requests.get(URL , headers = headers)
soup = BeautifulSoup(page.text, 'html.parser')
phones = soup.find_all('div' , attrs= {'class' : 's-result-item'})


a = []
b = []
c = []

for phone in phones:
    name = phone.find_all('span', attrs={'class': 'a-size-base a-color-base a-text-normal'})
    price = phone.find_all('span' , attrs = {'class' : 'a-offscreen'})
    rating = phone.find_all('span' , attrs = {'class' : 'a-icon-alt'})
    if(len(name) > 0):
        name = name[0].text
        if len(price)>0:
            price = price[0].text
        else:
            price = None

        if len(rating) > 0:
            rating = rating[0].text
        else:
            rating = None

        a.append(name)
        b.append(price)
        c.append(rating)

ans = []
for i in range(len(a)):
    ans.append([a[i] , b[i] , c[i]])


df = pd.DataFrame(ans , columns= ['Name' , 'Price' , 'Rating'])

ans = df.to_json(orient='records')

print(ans)
