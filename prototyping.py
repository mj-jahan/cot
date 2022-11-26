import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('price_data/USD_CAD.csv')
df.drop('Vol.', axis=1, inplace=True)
df.drop('Change %', axis=1, inplace=True)
df.drop('Open', axis=1, inplace=True)
df.drop('High', axis=1, inplace=True)
df.drop('Low', axis=1, inplace=True)
df.columns = ['Date', 'Close']

df = df.iloc[::-1]


def displaySpecificAsset(df):
    plt.plot(df['Date'], df['Close'])
    plt.title('USD/CAD Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()


print(df)
displaySpecificAsset(df)
