import pandas as pd

# load data
df = pd.read_csv('wines.csv')

# Count of wines with 100 points
data = len(df.loc[df['points'] == 100])
print(data)

# Name of most expensive wine
data = df.loc[df['price'] == df['price'].max()]['name'].squeeze()
print(data)

# New column that displays ratings from 0 to 5
df['ratings'] = df['points'] / 20
print(df['ratings'])

# Price histogram for wines that cost less than 100
df.loc[df['price'] < 100]['price'].hist()

# Plot price horizontally against points vertically
df.plot(x='price', y='points', kind='scatter')
