import pandas as pd

data = pd.read_csv(r"D:\Загрузки\3.3.2.csv", sep=";")

price = data['Price'].round()
mean_price = round(price.mean(), 1)
median_price = round(price.median(), 1)
std_price = round(price.std(), 1)

print(f"{mean_price} {median_price} {std_price}")