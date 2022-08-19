import requests
import codecs
from bs4 import BeautifulSoup
proxies = {"http": "http://10.1.11.50:8080",
           "https": "http://10.1.11.50:8080"}

r=requests.get("https://www.la-razon.com/economia/1/", proxies=proxies)
r=r.content.decode('utf-8','ignore')
soup = BeautifulSoup(r, 'html5lib')
###print("Encoding method :", soup.original_encoding)
''' divis = soup.find_all('div')
for divi in divis:
    print(divi)
 '''
###divisc = soup.find_all('div',class_='articles')#,limit=1)
''' for divi in divisc:
    if 'id' in divi.attrs:
        print("el id es: ", divi['id'])
 '''
''' pisis = soup.find_all('p')
for pis in pisis:
    print(pis) '''
arts = soup.find('div',id='lr-main')#,limit=1)
''' for art in arts:
    if 'a' in art.attrs:
        print("el a es: ", art['a'])
 '''
aa = arts.find_all('a',class_="link")
for a in aa:
    if 'href' in a.attrs:
        print("el a es: ", a['href'])
    #print(a.href.text)

