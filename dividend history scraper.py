#cleaning tool for html (and related) code
from bs4 import BeautifulSoup
import requests

#interacting with webpage (scrolling in our case)
from selenium import webdriver
import time

#let's you read/write json format data
import json
import pandas as pd

'''[]'''
'''
'ATVI',
'AYI',
'AVAV',
'AES',
'AL',
'MDRX',
'ABC',
'AMN',
'ANTM',
'AAPL',
'ARLO',
'OZK',
'OZK',
'BJRI',
'BKNG',
'BSX',
'CELG.RT',
'CNP',
'CRL',
'CSCO',
'C',
'CFG',
'COLM',
'XLC',
'XLY',
'XLP',
'GLW',
'CCI',
'DE',
'DK',
'FANG',
'DLR',
'DG',
'DHI',
'ETFC',
'EGBN',
'XLE',
'EOG',
'XOM',
'FB',
'FDX',
'XLF',
'FSLR',
'FBC',
'HAL',
'HCA',
'HCI',
'XLV',
'HD',
'HPQ',
'XLI',
'IART',
'KDP',
'KMI',
'KHC',
'KR',
'LH',
'LMT',
'MSGS',
'MMP',
'XLB',
'MU',
'MSFT',
'VTRS',
'NTGR',
'NYCB',
'NLSN',
'OXY',
'ONDK',
'PRTY',
'PWR',
'RRC',
'XLRE',
'SRG',
'SPG',
'SWKS',
'RDS.B',
'SPR',
'SQ',
'SBUX',
'SUPN',
'SYF',
'SYNH',
'XLK',
'TSLX',
'HEAR',
'TSN',
'ULTA',
'UPS',
'URI',
'XLU',
'VLO',
'WMT',
'WM',
'WCG',
'SEP',
'''
''''COLM',
'HD',
'TSN',
'ULTA',
'WMT',
'XLP',
'XLY',
'EOG',
'KMI',
'MMP',
'OXY',
'RDS.B',
'XLE',
'EGBN',
'ONDK',
'SPG',
'SYF',
'TSLX',
'WAL',
'XLF',
'XLRE',
'ABC',
'ANTM',
'HCA',
'SYNH',
'XLV',
'CSCO',
'MU',
'HEAR',
'XLK',
'AVAV',
'CNP',
'FDX',
'SPR',
'XLB',
'XLI',
'XLU',
'BKNG',
'XLC',
'BKR',
'CUBI',
'SEM',
'PGNY',
'MSFT',
'V',
'RGLD',
'TMUS',
'DISCA',
'FB',
'MCD',
'EPD',
'AINV',
'COLL',
'ASML',
'NGVT',
'WWE'''

tickers = [

'XLRE',

'XLV',

]



for i in range(len(tickers)):
    ticker = tickers[i]
    url = "https://www.nasdaq.com/market-activity/stocks/"+str(ticker)+ "/dividend-history"
    print(ticker)
    browser = webdriver.Chrome("C://Users//mzhu0//Downloads//chromedriver_win32 (1)//chromedriver.exe")
    browser.get(url)
    SCROLL_PAUSE_TIME = 0.5

    last_height = 1080

    for k in range(3):
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
        array = [tr.find("th")]
        array.extend(tr.find_all('td'))
        print(array)
        dict2 = {}
        #index1 = array[0].find('">')
        #index2 = array[0].find('</span>')
        try:
            dict2['Ex Date'] = array[0].text
            dict2['TYPE'] = array[1].text
            dict2['Cash amount'] = array[2].text
            dict2['Dec date'] = array[3].text
            dict2['record date'] = array[4].text
        except:
            continue

        dict[array[5].text] = dict2

    file_name = str(tickers[i])
    with open(file_name, "w") as file2:
        json.dump(dict, file2)

    browser.close()

print("Good job")