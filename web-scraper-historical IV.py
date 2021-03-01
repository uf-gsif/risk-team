
#let's you access data from urls (can also use urllib)
import requests

#let's you read/write json format data
import json

#read file with json data
def read_dict(file_name):
    f = open(file_name, 'r')
    tickers = json.loads(f.read())
    return tickers


companies = read_dict("ticker-list.json")
print(companies)
tickers = []
for thing in companies:
    tickers.append(thing["ticker"])

print(tickers)

for ticker in tickers:
    url = "https://www.alphaquery.com/data/option-statistic-chart?ticker=" +str(ticker)+ "&perType=30-Day&identifier=iv-mean"
    data = requests.get(url)
    file_name = str(ticker) + "-IV"

    if 'No data available for the given symbol.' in data.text:
        continue

    with open(file_name, "w") as file2:
        json.dump(data.text, file2)

print("Good job!")


