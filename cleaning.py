import pandas as pd

# This Python script is to clean the file and save the file for further analysis.


# Loading data from google drive
path = 'datasets/africa_food_prices.csv'
df = pd.read_csv(path)

    # Renaming first column.
df.rename({'Unnamed: 0':'id'}, axis =1, inplace =  True)

    # Decongesting dataframe
del df['country_id']
del df['state_id']
del df['market_id']
del df['produce_id']
del df['currency_id']
del df['pt_id']
del df['um_unit_id']
del df['mp_commoditysource']

    # Transforming df['id'], df['month'] and df['year'] to dtype str.
df['id'] = df['id'].astype('str')
df['month'] = df['month'].astype('str')
df['year'] = df['year'].astype('str')

    # Creating another column df['day'] to contain value '1'(as text type).
    # This means we only recognize the first of the month in the dataset.
df['day'] = '1'

    # Concatenating df['year'], df['month'] and df['year'] with seperator '-'
df['date'] = df['day']+'-'+df['month']+'-'+df['year']
df['date'] = df['date'].astype('str')

    # Converting df['date'] to pandas date type.
df['date']=df['date'].apply(pd.to_datetime, utc = False)

    # Filling the null values in df['state'] with df['country'] values.
df['state'].fillna(df['country'], inplace = True)

    # Saving cleaned dataset
df.to_parquet('datasets/cleaned_food_prices.parquet')
