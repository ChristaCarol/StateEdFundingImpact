# src/data/convert_rate.py
def convert_rate(rate):
    """
    Convert RATE column values into a consistent numeric format.
    
    This function handles various formats found in the RATE column, including
    numeric rates, ranges, and special codes ('GE' for greater than or equal to,
    and 'PS' for data privacy suppressed). Ranges are converted to their midpoint,
    'GE' codes are converted to their numeric part, and 'PS' or other non-numeric
    values are handled as NaN.
    
    Parameters:
    - rate (str): The RATE column value to be converted.
    
    Returns:
    - float or np.nan: The converted rate as a float, or np.nan for non-numeric values.
    """
    if pd.isnull(rate):
        return np.nan
    if '-' in rate:
        low, high = rate.split('-')
        return (float(low) + float(high)) / 2
    elif rate.isdigit():
        return float(rate)
    elif 'GE' in rate:
        return float(rate.replace('GE', ''))
    else:
        return np.nan
