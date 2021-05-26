from pprint import pprint
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
import pandas as pd

url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=pawapro&_sacat=0'



d_list = []
for i in range(1,5):
    print(len(d_list))
    target_url = url.format(i)
    r = requests.get(target_url)
    sleep(1)
    soup = BeautifulSoup(r.text)

    contents = soup.find_all('div', class_='s-item__wrapper clearfix')

    for content in contents:

        detail = content.find('div', class_='s-item__info clearfix')
        image_url = content.find('img', class_='s-item__image-img')

        title = detail.find('h3', class_='s-item__title')
        priem = detail.find('span', class_='s-item__price')
        ul = detail.find('a')

        if title and priem is not None:
            d = {
                'title': title.text,
                'priem': priem.text,
                #'url': ul
            }

            d_list.append(d)

pprint(d_list)

df = pd.DataFrame(d_list)
df.to_csv('test.csv',index=None, encoding='utf-8-sig')