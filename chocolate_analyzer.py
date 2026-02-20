import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading data from the CSV file into a DataFrame
df = pd.read_csv('ChocolateSales.csv')

#Data before cleaning
print('--- Data Before Being Cleaned ---\n')
print(df.head())

#Cleaning my data by removing the $ sign and converting to float
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)

#Converting date into datetime objects
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

#Creating columns to use for analysis
df['Price Per Box'] = df['Amount'] / df['Boxes Shipped']
df['Year Month'] = df['Date'].dt.to_period('M')

print('\nData cleaning complete. Ready for analysis! Here is a sample below.\n')
print(df.head())
