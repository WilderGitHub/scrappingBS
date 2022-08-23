import requests
import codecs
import html
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import re
import html
import pandas as pd
from requests import get

proxies = {"http": "http://10.1.11.50:8080","https": "http://10.1.11.50:8080"}

r=requests.get("https://www.la-razon.com/economia/page/1/", proxies=proxies)
r=r.content.decode('windows-1252','ignore')
soup = BeautifulSoup(r, 'html5lib')
###print("Encoding method :", soup.original_encoding)

###################################
### Encontramos el cuerpo principal de los articulos
arts = soup.find('div',id='lr-main')
# Encontramos los links de los articulos
links = arts.find_all('a',class_="link")
listalinks=[]
for a in links:
    if 'href' in a.attrs:
        ##print("el a es: ", a['href'])
        listalinks.append(a['href'])
    #print(a.href.text)
####print("esta seriya la lista: ",listalinks)
print("numero de links", len(links))
############################
### Encontramos el id de cada articulo
for n in range(len(links)): 
    print("---- inicio ---------  ", n)
    r=requests.get(listalinks[n], proxies=proxies)
    r=r.content.decode('windows-1252',errors='ignore')
    articulos = BeautifulSoup(r, 'html5lib')
    elarticulo = articulos.find('div',id="lr-main")
    
    ids=[]
    
    indice=elarticulo.find_next(id)
    #print("el id es: ",indice)
    # indices=elarticulo.find_all(id)#,limit=4) #sabemos que esta en un cuerto nivel
    #for id in indice:
    print("indicesdsd",indice.id)
    if 'id' in indice.attrs:
        print("los id de los divs son: ",indice['id'])
    #id=id['id']
    #print("el id es: ",id) 
    #ids=[]

    titular=elarticulo.find_next("h1").text#, id="article679331")
    titulares=[]
    titulares.append(titular)
    print("el titular es: ", titulares)
    #######  Encontramos el texto
    detalle = elarticulo.find_next('p').text

    detalles=[]
    detalles.append(detalle)
    print("el detalle es: ", detalles)

    divsparrafos = elarticulo.find_next('div',class_="article-body")

    print("el parrafo es:")

    parrafos=divsparrafos.findChildren('p')
    parrafoses=[]
    for pp in parrafos:
        parrafoses.append(pp)
        unparrafo=' '.join(map(str,parrafoses)).replace("</p> <p>"," ").replace("<p>","").replace("</p>","")
    print(unparrafo)
    print("---- fin ---------")