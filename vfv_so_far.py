# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DIP0EdyReaArmd-1-vYIZ6CkAcupaRPT
"""

pip install yfinance

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn import linear_model

d = yf.download("VFV.TO", start = "2012-11-05", end = "2021-04-30")
print(d)

df = pd.read_csv("/content/VFV_prices.csv")
print(df)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel("Days")
plt.ylabel("Prices(CA$)")
plt.scatter(df["Days"], df["Adj Close"])

reg = linear_model.LinearRegression()
reg.fit(df[["Days"]], df["Adj Close"])

print(reg.predict([[2127]]))