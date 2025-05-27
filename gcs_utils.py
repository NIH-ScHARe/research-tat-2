import pandas as pd

def get_cancer_data(filepath):
    """
    Load cancer data from a CSV file and return it as a DataFrame.
    
    Returns:
        pd.DataFrame: A DataFrame containing the cancer data.
    """
    # Read in the CSV file with cancer data
    cancer_data = pd.read_csv(filepath,header=1)

    # Make sure the FIPS code is a string and zero-padded to 5 digits
    cancer_data['FIPS'] = cancer_data['County FIPS'].astype(str).str.zfill(5)

    # convert the cancer rate column to numeric, forcing errors to NaN
    cancer_data['mortality_rate'] = pd.to_numeric(cancer_data['Age-Adjusted Rate per 100,000'], errors='coerce')

    return cancer_data