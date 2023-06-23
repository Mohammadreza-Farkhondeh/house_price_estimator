import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('price_estimator/home_file.csv')

df['Area'] = pd.to_numeric(df['Area'], errors='coerce')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

df.dropna(subset=['Area'], inplace=True)
df.dropna(subset=['Price'], inplace=True)


df = df.replace(True,1)
df = df.replace(False,0)

df['Area_Price'] = df["Price"] / df['Area']
df.dropna(subset=['Address'], inplace=True)

avg_prices_by_address = df.groupby('Address')['Price'].mean()


avg_prices_by_address = df.groupby('Address')['Price'].mean().reset_index()
avg_prices_by_address = avg_prices_by_address.rename(columns={'Price': 'AvgPrice'})

df = pd.merge(df, avg_prices_by_address, on='Address')

df.to_csv('your_updated_file_name.csv', index=False)

df =pd.read_csv('your_updated_file_name.csv')


result = [(y, x) for x, y in zip(avg_prices_by_address['Address'], avg_prices_by_address['AvgPrice'])]

# print(result)

