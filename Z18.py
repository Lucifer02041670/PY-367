import pandas as pd

data = pd.read_csv("3.3.2.csv", sep=";")

data['Time of deal'] = pd.to_datetime(data['Time of deal'])

data['Hour'] = data['Time of deal'].dt.hour
hour = data['Hour'].mode()[0]

print(hour)
