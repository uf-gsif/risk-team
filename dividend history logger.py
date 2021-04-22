import pandas as pd
import json

df = pd.read_excel("C:/Users/mzhu0/PycharmProjects/GSIF/dividend history 2020.xlsx").astype(str)
print(df)
tickers = list(df)[1:]
print(tickers)
count =0
for file in tickers:
    try:
        with open('C://Users//mzhu0//PycharmProjects//GSIF//dividend_history 2020//'+str(file)) as f:
            data = json.load(f)
    except:
        continue
    if(len(data)==0):
        continue
    else:
        index =0
        for date in df["Date"]:
            for key in data.keys():
                if data[key]["Ex Date"][-4:] == date[:4] and data[key]["Ex Date"][3:5] == date[-2:] and data[key]["Ex Date"][:2] == date[5:7]:
                    df.at[index, file] = float(data[key]["Cash amount"][1:])
                    count = count+1
            index = index + 1
df = df.replace('nan', 0)
df.to_excel("dividend_history_gsif_2020.xlsx")