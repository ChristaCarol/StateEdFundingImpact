# src/data/clean_data.py
def flatten_columns_and_rename(df, rename_dict=None):
    """
    Flatten MultiIndex columns and rename specific columns based on a given dictionary.
    
    Parameters:
    - df: DataFrame with potentially MultiIndex columns.
    - rename_dict: Dictionary mapping old column names to new ones (optional).
    
    Returns:
    - DataFrame with flattened column names and renamed columns.
    """
    # Flatten MultiIndex columns if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ['_'.join(col).strip() for col in df.columns.values]
    
    # Rename specific columns if a dictionary is provided
    if rename_dict:
        df.rename(columns=rename_dict, inplace=True)
    
    return df
