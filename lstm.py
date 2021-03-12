import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from sklearn.preprocessing import RobustScaler
plt.style.use("bmh")
from ta import add_all_ta_features
from ta.utils import dropna

#technical analysis lib
# import ta

#nn lib
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

#load data
df = pd.read_csv("NIO.csv")
print(df)

#dateime convertion
df['Date'] = pd.to_datetime(df.Date)

#set the index
df.set_index('Date', inplace = True)
 
#Drop Nans
df = dropna(df)

#tech indc
df = add_all_ta_features(df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True)

#only use last 100 days


