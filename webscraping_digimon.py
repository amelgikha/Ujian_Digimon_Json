from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

req = requests.get('http://digidb.io/digimon-list/')
soup=BeautifulSoup(req.content,'html.parser')
# print(soup.prettify())

data = soup.find('table', id='digiList')

digimon=[]
data=data.find_all('tr')
for i in data[1:]:
    no = i.td.string
    nama = i.a.string
    gambar = i.img['src']
    stage = i.center.string
    tipe = i.td.find_next_sibling().find_next_sibling().find_next_sibling()
    attribute = i.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()
    memory = attribute.find_next_sibling()
    equip = memory.find_next_sibling()
    hp = equip.find_next_sibling()
    sp = hp.find_next_sibling()
    atk = sp.find_next_sibling()
    defense = atk.find_next_sibling()
    intt = defense.find_next_sibling()
    spd = intt.find_next_sibling()
    x={
        'no':int(no),
        'digimon':nama,
        'image':gambar,
        'stage':stage,
        'type':tipe.string,
        'attribute':attribute.string,
        'memory':memory.string,
        'equip slots':equip.string,
        'hp':hp.string,
        'sp':sp.string,
        'atk':atk.string,
        'def':defense.string,
        'int':intt.string,
        'spd': spd.string}
    digimon.append(x)
print(digimon)


with open('dataDigi.json','w') as x:
    x.write(str(digimon).replace("'",'"'))


    
