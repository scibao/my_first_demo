import tushare as ts
import pandas as pd
import datetime

#1.get tickers
tickersRawData =ts.get_stock_basics()
tickers = tickersRawData.index.tolist()
#print(tickers)

#2.save tickers
dateToday = datetime.datetime.today().strftime('%Y%m%d')
file = 'E:\\python\\stock\\stockdata\\tickerlist_'+dateToday+'.csv'
tickersRawData.to_csv(file)
print('tickers saved')
