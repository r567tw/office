import requests
import pandas as pd
import matplotlib.pyplot as plt

data = requests.get("https://www.coingecko.com/price_charts/1/twd/max.json")
# response type can use json() => dict type => list type
prices = data.json()["stats"]

# print(type(prices))
df = pd.DataFrame(prices, columns=["Datetime", "TWD"])
df["Datetime"] = pd.to_datetime(df["Datetime"], unit="ms")
# df["TWD"] = pd.to_numeric(df["TWD"])
df.index = df["Datetime"]
# 每一百個位數取前一百的平均，rolling=>移動平均
df["ma"] = df["TWD"].rolling(window=100).mean()
# print(df.head())
df[["TWD", "ma"]].plot(kind="line", figsize=[10, 5])
plt.show()
