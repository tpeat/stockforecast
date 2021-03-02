import numpy as np
import pandas as pandas
import matplotlib.pyplot as plt
import yfinance as yf
import json


tickers = yf.Tickers(['msft', 'nio', 'dkng'])

#getting info
info = tickers.tickers.NIO.info
# print('Info: ')
# print(json.dumps(info, indent=2))

history = tickers.tickers.MSFT.history(period="max")

print("history: ")
print(history)