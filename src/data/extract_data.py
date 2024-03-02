# src/data/extract_data.py
import pandas as pd

def extract_data(file_path):
    """Extract data from a given file path."""
    data = pd.read_csv(file_path)
    print(data.columns)
    return data
