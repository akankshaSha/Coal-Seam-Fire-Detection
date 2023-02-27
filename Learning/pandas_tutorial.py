## Why Pandas?
#    - flexiblity
#    - working with Big Data

#%% loading data into Pandas

import pandas as pd

# reads files into data frames
df = pd.read_csv('pokemon_data.csv')

print(df)

## see head or tail (default rows = 5)
print(df.head())
print(df.tail(3))

# to read excel use pd.read_excel
# change delimeters to read tab separated file as
# pd.read_csv('filepath', delimiter = '\t')


#%% reading data

## read headers
print(df.columns)

## read each column
print(df['Name'][0:5])
print(df[['Name', 'Type 1', 'HP']])
print(df.Name)

## reach each row
print(df.iloc(0)) # integer location
print(df.iloc[2:10])

## read a specific location [r, c]
print(df.iloc[2, 1])


#%% iterating

for index, row in df.iterrows():
    print(index, row['Name'])


#%% getting rows based on pecific condition

print(df.loc[df['Type 1'] == 'Grass'])


#%% High Level description of your data (min, max, mean, std dev, etc.)

print(df.describe())

#%% Sorting Values (Alphabetically, Numerically)

print(df.sort_values('Name', ascending = False))
print(df.sort_values(['Type 1', 'HP'], ascending = [1, 0]))

#%% Making Changes to the DataFrame
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

print(df.head())


#%% Adding a column

#%% Deleting a column

df = df.drop(columns=['Total'])
print(df.head())


#%% Summing Multiple Columns to Create new Column.

df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head())


#%% Rearranging columns

df = df[['Name', 'Total', 'Type 1', 'Type 2']]
print(df.head())

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

print(df.head())


#%% Saving our Data (CSV, Excel, TXT, etc.)

df.to_csv('modified.csv', index = False)

# df.to_excel('filename.xlsx')
# df.to_csv('filename.txt', sep='\t')

#%% Filtering Data (based on multiple conditions)

#%% Reset Index

#%% Regex Filtering (filter based on textual patterns)

#%% Conditional Changes

#%% Aggregate Statistics using Groupby (Sum, Mean, Counting)

#%% Working with large amounts of data (setting chunksize)

