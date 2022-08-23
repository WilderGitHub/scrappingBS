from ipaddress import collapse_addresses
from os import sep
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from requests import get
import locale
from datetime import datetime as dt

proxies = {"http": "http://10.1.11.50:8080","https": "http://10.1.11.50:8080"}

desde=3600
hasta=3600
pasito=1
columnas=["codigo","fecha","titular","detalle","texto"]
consolidado=pd.DataFrame()
for pagina in range(desde,hasta+1,pasito):
    url = "https://www.la-razon.com/economia/page/" + str(pagina)
    r=requests.get(url, proxies=proxies)
    #r=r.content.decode('windows-1252','ignore')
    r=r.content.decode('utf-8','ignore')
    soup = BeautifulSoup(r, 'html5lib')
    ###################################
    ### Encontramos el cuerpo principal de los articulos
    arts = soup.find('div',id='lr-main')
    # Encontramos los links de los articulos
    links = arts.find_all('a',class_="link")
    listalinks=[]
    for a in links:
        if 'href' in a.attrs:
            listalinks.append(a['href'])
    #print("numero de links", len(links))
    ############################
    ### Encontramos el id de cada articulo
    ids=[]
    fechas=[]
    titulares=[]
    detalles=[]
    textos=[]
    for n in range(len(links)): 
        #print("---- inicio ---------  ", n)
        r=requests.get(listalinks[n], proxies=proxies)
        r=r.content.decode('utf-8',errors='ignore')
        articulos = BeautifulSoup(r, 'lxml')#html5lib')
        elarticulo = articulos.find('div',id="lr-main")
        #######  Encontramos el id
        
        indice=elarticulo.find_next(id).find_next(id).find_next(id).find_next(id)
        #print("el id es: ",indice['id'])
        ids.append(indice['id'])
        #######  Encontramos la fecha
        
        
        locale.setlocale(locale.LC_TIME, '')
        try:
            fecha=elarticulo.find_all('span',limit=2)[1].text    
            mifecha = dt.strptime(fecha, ' / %d de %B de %Y')
        except:
            fecha=elarticulo.find_all('span',limit=2)[0].text    
            mifecha = dt.strptime(fecha, ' / %d de %B de %Y')
        else:#except ValueError:
            fecha=elarticulo.find_all('span',limit=2)[1].text    
            mifecha = dt.strptime(fecha, ' / %d de %B de %Y')
               #print("La fecha es: ",mifecha)
        fechas.append(mifecha)
        #######  Encontramos el titular
        titular=elarticulo.find_next("h1").text
        titulares.append(titular)
        #print("el titular es: ", titulares)
        
        #######  Encontramos el detalle
        detalle = elarticulo.find_next('p').text
        detalles.append(detalle)
        #print("el detalle es: ", detalles)
        #######  Encontramos el texto
        divsparrafos = elarticulo.find_next('div',class_="article-body")
        parrafos=divsparrafos.findChildren('p')
        parrafoses=[]
        for pp in parrafos:
            parrafoses.append(pp.string)
            unparrafo=' '.join(map(str,parrafoses))#.replace("</p> <p>"," ").replace("<p>","").replace("</p>","")
        textos.append(unparrafo)
    
    troso=pd.DataFrame(list(zip(ids, fechas, titulares,detalles,textos)),columns=columnas)
    
    consolidado= consolidado.append(troso, ignore_index=True)
#print("consolidado: ", consolidado.head(20))
#consolidado.to_excel("prueba.xlsx", encoding='utf8')    
consolidado.to_csv("prueba.csv", encoding='utf8',sep="|")    