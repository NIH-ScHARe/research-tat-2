import pandas as pd

def find_missing_rows(data, column_name):
    """
    Find rows in the DataFrame where the specified column has missing values.
    
    Args:
        data (pd.DataFrame): The DataFrame to check.
        column_name (str): The name of the column to check for missing values.
        
    Returns:
        pd.DataFrame: A DataFrame containing rows with missing values in the specified column.
    """
    return data[data[column_name].isnull()]

def clean_target_feature(data, column_name):
    """
    Clean the target feature by dropping rows with NaN values in the specified column.
    
    Args:
        data (pd.DataFrame): The DataFrame to clean.
        column_name (str): The name of the target feature column to clean.
    Returns:
        pd.DataFrame: The DataFrame with rows containing NaN in the specified column removed.    
    """
    return data.dropna(subset=column_name)

def clean_features(data):
    """
    Clean the features in the DataFrame by performing a median imputation for missing values.
    Args:
        data (pd.DataFrame): The DataFrame to clean.    
    
    Returns:
        pd.DataFrame: The DataFrame with missing values in numeric columns filled with the median of each column.
    """
    # make a copy of the data to avoid modifying the original DataFrame
    data = data.copy()

    # get names of feature columns (all columns except 'FIPS')
    feature_columns = [col for col in data.columns if col != 'FIPS']
    
    # fill NaN values in feature columns with the median of each column
    for column in feature_columns:
        if data[column].dtype in ['float64', 'int64']:
            data[column] = data[column].fillna(data[column].median())

    return data

def clean_dataset(raw_dataset):
    """
    Clean the dataset by removing rows with missing values in the 'mortality_rate' column.
    
    Args:
        dataset (pd.DataFrame): The dataset to clean.
        
    Returns:
        pd.DataFrame: The cleaned dataset with rows containing NaN in 'mortality_rate' removed.
    """

    # clean the target feature 
    target_cleaned = clean_target_feature(raw_dataset, 'mortality_rate')

    # clean the features 
    feature_cleaned = clean_features(target_cleaned)
    
    # save cleaned dataset to csv
    feature_cleaned.to_csv('dataset_cleaned.csv', index=False)

    return feature_cleaned 

