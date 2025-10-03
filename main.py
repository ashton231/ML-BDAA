import pandas as pd
import numpy as np
import matplotlib

dfETFs = pd.read_csv("ETFs/aadr.us.txt", sep=",")
print(dfETFs.head())
print(dfETFs.shape)

dfStocks = pd.read_csv("Stocks/a.us.txt", sep=",")
print(dfStocks.head())
print(dfStocks.shape)