# src/data/transform_data.py
import pandas as pd

def concatenate_dataframes(dfs):
    """Concatenate a list of DataFrames."""
    return pd.concat(dfs, ignore_index=True)

def transform_data(df, id_vars):
    """Transform the DataFrame into a long format and pivot as required."""
    transformed_df = pd.melt(df, id_vars=id_vars, var_name='CATEGORY', value_name='VALUE')
    # Add more transformation steps as needed
    return transformed_df
