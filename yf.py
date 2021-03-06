import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import json



tickers = yf.Tickers(['msft', 'nio', 'dkng', 'spy'])

#getting info
info = tickers.tickers.NIO.info
# print('Info: ')
# print(json.dumps(info, indent=2))

history = tickers.tickers.SPY.history(period="max", actions=False)

data = yf.download(tickers.tickers.SPY.history(period="max", actions=False))

print("history: ")

