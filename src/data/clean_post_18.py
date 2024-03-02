# src/data/clean_post_18.py

import pandas as pd
import numpy as np

def convert_rate(rate):
    """Convert rate values into a consistent numeric format."""
    if pd.isnull(rate):
        return np.nan
    rate = str(rate)
    if '-' in rate:
        low, high = rate.split('-')
        return (float(low) + float(high)) / 2
    elif rate.isdigit():
        return float(rate)
    elif 'GE' in rate:
        return float(rate.replace('GE', ''))
    else:
        return np.nan

def clean_post_18(df):
    """Clean and transform DataFrames for post-2018 data."""
    # Rename 'STNAM' to 'STATE'
    df.rename(columns={'STNAM': 'STATE'}, inplace=True)
    
    # Convert RATE using the numerical transformation
    df['RATE_NUMERIC'] = df['RATE'].apply(convert_rate)
    
    # Aggregate data by 'SCHOOL_YEAR' and 'STATE'
    aggregated_df = df.groupby(['SCHOOL_YEAR', 'STATE']).agg({
        'COHORT': 'sum',
        'RATE_NUMERIC': 'mean'
    }).reset_index()
    
    # Set 'SCHOOL_YEAR' back as the index
    aggregated_df.set_index('SCHOOL_YEAR', inplace=True)
    
    return aggregated_df
