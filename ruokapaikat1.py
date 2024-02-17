from bs4 import BeautifulSoup
import requests
from aika import *

ruokalista = []

def hulluorava():
    html_text = requests.get('https://www.lounaat.info/lounas/cafe-hullu-orava/lappeenranta').text
    soup = BeautifulSoup(html_text,'lxml')
    ruuat1 = soup.find_all('div', class_="item")
    for ruuat in ruuat1:
        ruokalista.append(ruuat.text.strip())
    
def panchovilla():
    html_text = requests.get('https://www.lounaat.info/lounas/pancho-villa/lappeenranta').text
    soup = BeautifulSoup(html_text,'lxml')
    ruuat2 = soup.find_all('div', class_="item")
    for ruuat in ruuat2:
        ruokalista.append(ruuat.text.strip())

def wolkoff():
    html_text = requests.get('https://wolkoff.fi/ruoka-juoma/').text
    soup = BeautifulSoup(html_text,'lxml')
    ruuat3 = soup.find_all('li', class_="menu-list__item")
    for ruuat in ruuat3:
        ruokalista.append(ruuat.text.strip())

def kolmekivea():
    html_text = requests.get('https://www.lounaat.info/lounas/httpskolmekiveafiravintolawillhelmiina/lappeenranta').text
    soup = BeautifulSoup(html_text,'lxml')
    ruuat4 = soup.find_all('div', class_="item")
    for ruuat in ruuat4:
        ruokalista.append(ruuat.text.strip())

def miku():
    html_text = requests.get('https://www.ruokapaikka.fi/#id=2013346&n=Cafe%20Miku').text
    soup = BeautifulSoup(html_text,'lxml')
    ruuat5 = soup.find_all('li', class_="menu-list__item")
    for ruuat in ruuat5:
        ruokalista.append(ruuat.text.strip())

def Vapari():
    html_text1 = requests.get('https://www.lounaat.info/lounas/food-co-vapari/lappeenranta').text
    soup = BeautifulSoup(html_text1, 'lxml')
    ruuat6 = soup.find_all('div', class_ = 'item')
    for ruuat in ruuat6:
        ruokalista.append(ruuat.text.strip())

def Kitchen():
    html_text = requests.get('https://www.lounaat.info/lounas/the-kitchen/lappeenranta').text
    soup = BeautifulSoup(html_text, 'lxml')
    ruuat7 = soup.find_all('div', class_ = 'item')
    for ruuat in ruuat7:
        ruokalista.append(ruuat.text.strip())

def elsi():
    html_text = requests.get('https://www.lounaat.info/lounas/lounaskahvila-elsi/lappeenranta').text
    soup = BeautifulSoup(html_text,'lxml')
    ruuat8 = soup.find_all('div', class_="item")
    for ruuat in ruuat8:
        ruokalista.append(ruuat.text.strip())

def kehruuhuone():
    html_text = requests.get('https://www.lounaat.info/lounas/kehruuhuone/lappeenranta').text
    soup = BeautifulSoup(html_text,'lxml')
    ruuat9 = soup.find_all('div', class_="item")
    for ruuat in ruuat9:
        ruokalista.append(ruuat.text.strip())


def etsi():

    item_ruoka = []
    for data in ruokalista:
        if isinstance(data, str):
            if inputText in data:
                item_ruoka.append(data.strip())
    if item_ruoka:
        for i, item in enumerate(item_ruoka):
            print(f" {i+ 1}: \n{item}\n")
        else:
            print("Ei ruokailua")

hulluorava()
panchovilla()
wolkoff()
kolmekivea()
miku()
Vapari()
Kitchen()
elsi()
kehruuhuone()
etsi()