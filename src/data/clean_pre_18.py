# src/data/clean_pre_18.py

import pandas as pd
import numpy as np

def convert_rate(rate):
    """Converts rate values into a consistent numeric format."""
    # First, check if rate is NaN (float), return np.nan to avoid trying to iterate over it
    if pd.isnull(rate):
        return np.nan
    
    # Ensure rate is treated as a string for the following operations
    rate = str(rate)
    
    if '-' in rate:
        low, high = rate.split('-')
        return (float(low) + float(high)) / 2  # Return midpoint of range
    elif rate.isdigit():
        return float(rate)
    elif rate.startswith('GE'):
        return float(rate.replace('GE', ''))
    else:  # Handle 'PS' and other non-numeric codes
        return np.nan  # Convert non-numeric rates to NaN or a specific value as needed


def clean_pre_18(df):
    """Cleans and transforms DataFrame for pre-2018 datasets."""
    id_vars = ['STNAM', 'LEANM', 'DATE_CUR']
    
    # Melt the dataframe
    transformed_df = pd.melt(df, id_vars=id_vars, var_name='CATEGORY', value_name='VALUE')
    
    # Extract 'GROUP' and 'DATA_TYPE' from 'CATEGORY'
    transformed_df[['GROUP', 'DATA_TYPE']] = transformed_df['CATEGORY'].str.rsplit('_', n=2).apply(pd.Series)[[0, 1]]
    
    # Pivot the DataFrame
    pivoted_df = transformed_df.pivot_table(index=['STNAM', 'LEANM', 'GROUP', 'DATE_CUR'], 
                                            columns='DATA_TYPE', 
                                            values='VALUE', 
                                            aggfunc='first').reset_index()

    # Flatten columns and rename them
    if isinstance(pivoted_df.columns, pd.MultiIndex):
        pivoted_df.columns = ['_'.join(col).strip() for col in pivoted_df.columns.values]

    # Rename columns
    pivoted_df.rename(columns={'STNAM': 'STATE'}, inplace=True)
    
    # Convert RATE values to numeric
    pivoted_df['RATE_NUMERIC'] = pivoted_df['RATE'].apply(convert_rate)
    
    # Aggregate data by state
    states_aggregated = pivoted_df.groupby('STATE').agg({
        'COHORT': 'sum',  # Summing all cohorts within the state
        'RATE_NUMERIC': 'mean'  # Mean of the numeric RATEs
    }).reset_index()
    
    states_aggregated.rename(columns={'RATE_NUMERIC': 'PERCENT_RATE'}, inplace=True)
    
    return states_aggregated

# Example usage:
# df = pd.read_csv('path_to_your_csv_file.csv')
# cleaned_df = clean_pre_2018(df)
# print(cleaned_df.head())
