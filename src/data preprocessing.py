import pandas as pd
import numpy as np

def load_raw_dataset(path):
    return pd.read_csv(path)

def clean_year(df):
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df.loc[(df['year'] < 860) | (df['year'] > 2025), 'year'] = np.nan
    df['year'] = df['year'].fillna(df['year'].median())
    return df

def clean_mass(df):
    df['mass (g)'] = pd.to_numeric(df['mass (g)'], errors='coerce')
    df['mass (g)'] = df['mass (g)'].fillna(df['mass (g)'].median())
    return df

def clean_coordinates(df):
    df['reclat'] = pd.to_numeric(df['reclat'], errors='coerce')
    df['reclong'] = pd.to_numeric(df['reclong'], errors='coerce')
    df['reclat'] = df['reclat'].fillna(df['reclat'].median())
    df['reclong'] = df['reclong'].fillna(df['reclong'].median())
    return df
