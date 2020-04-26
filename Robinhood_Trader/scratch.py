#TEST OF THE PYEX API FOR GENERATING MACD FOR SPECIFIC STOCK

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pyEX as p
ticker = 'MDT'
timeframe = '1h'
df = p.chartDF(ticker, timeframe)
df = df[['close']]
df.reset_index(level=0, inplace=True)
df.columns=['ds','y']
plt.plot(df.ds, df.y, label=ticker)
plt.show()