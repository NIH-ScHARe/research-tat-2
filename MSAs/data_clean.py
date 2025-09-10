import pandas as pd

def drop_incomplete_msas(df, msa_col="msa_code", year_col="year"):
    """
    Drops entire MSAs from the dataframe if they have 
    any missing values in any year.
    
    Parameters
    ----------
    df : pd.DataFrame
        The input dataframe (long format: one row per MSA-year).
    msa_col : str
        The column name identifying the MSA.
    year_col : str
        The column name identifying the year.
        
    Returns
    -------
    pd.DataFrame
        A filtered dataframe containing only MSAs with complete data.
    """
    # Find MSAs that have *no missing values* across all rows
    complete_msas = (
        df.groupby(msa_col)
          .filter(lambda g: not g.isnull().any().any())[msa_col]
          .unique()
    )
    
    # Keep only those MSAs
    return df[df[msa_col].isin(complete_msas)].copy()

def clean_data():
    data = pd.read_csv('MSAs/data/data_00_raw.csv')
    data = drop_incomplete_msas(data, msa_col="msa_code", year_col="year")
    data.to_csv('MSAs/data/data_01_clean.csv', index=False)