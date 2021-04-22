#let's you access data from urls (can also use urllib)
import requests

#cleaning tool for html (and related) code
from bs4 import BeautifulSoup

#interacting with webpage (scrolling in our case)
from selenium import webdriver
import time

#let's you read/write json format data
import json
import pandas as pd

from os import listdir

#get file names (just the stocks we have IV data for)
names = [file[:-3] for file in listdir('C://Users//mzhu0//PycharmProjects//GSIF//IV data')]
print(names)
#names_df = pd.DataFrame(names,columns=["Ticker"])
#names_df.to_csv("good_tickers.txt",index=False, header= True)

for ticker in names:
    url = 'https://finance.yahoo.com/quote/'+str(ticker)+'/history?period1=1293840000&period2=1616112000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

    browser = webdriver.Chrome("C://Users//mzhu0//Downloads//chromedriver_win32 (1)//chromedriver.exe")
    browser.get(url)
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height

    last_height = 1080#driver.execute_script("return document.body.scrollHeight")

    for i in range(30):
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, "+str(last_height)+");")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        last_height = last_height*2 #driver.execute_script("return document.body.scrollHeight")
        '''
        if new_height == last_height:
            break
        '''
        #last_height = new_height


    messy_data = browser.page_source

    #messy_data = requests.get(url)
    bsoup = BeautifulSoup(messy_data, 'html.parser')
    print(bsoup.find("tbody").find_all('tr'))
    bsoup2 = bsoup.find("tbody").find_all('tr')

    dict = {}
    for tr in bsoup2:
        array = tr.find_all('td')
        dict2 = {}
        #index1 = array[0].find('">')
        #index2 = array[0].find('</span>')
        try:
            dict2['open'] = array[1].find('span').text
            dict2['high'] = array[2].find('span').text
            dict2['low'] = array[3].find('span').text
            dict2['close'] = array[4].find('span').text
            dict2['adj_close'] = array[5].find('span').text
            dict2['mrktcap'] = array[6].find('span').text
        except:
            continue

        dict[array[0].find("span").text] = dict2

    file_name = str(names[0])
    with open(file_name, "w") as file2:
        json.dump(dict, file2)

    browser.close()

#.find('div',class_='Pb(10px) Ovx(a) W(100%)'))#class_='Pos(r) Bgc($bg-content) Bgc($lv2BgColor)! Miw(1007px) Maw(1260px) tablet_Miw(600px)--noRightRail Bxz(bb) Bdstartc(t) Bdstartw(20px) Bdendc(t) Bdends(s) Bdendw(20px) Bdstarts(s) Mx(a)'))

