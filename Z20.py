import pandas as pd

data = pd.read_csv("3.3.2.csv", sep=";")

bins = [0, 35, 55, float('inf')]
labels = ['Young', 'Middle-aged', 'Senior']
data['Age'] = pd.cut(data['Agent age'], bins=bins, labels=labels)

age = data['Age'].mode()[0]

print(age)