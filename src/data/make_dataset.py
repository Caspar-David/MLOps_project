import pandas as pd

df = pd.read_csv("./src/data/weatherAUS.csv", sep = ",")

print(df.head())