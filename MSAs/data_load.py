import pandas as pd 
from acs_utils import get_race_data 

def load_mortality_data() -> pd.DataFrame:
    """
    Load the mortality rate data from the CDC WONDER database and preprocess it. 
    
    Returns:
        MortalityDataFrameModel: A model containing the MSA, MSA code, year, and age-adjusted mortality rate DataFrame.
    """

    # load mortality data from the csv file 
    mortality_data = pd.read_csv('data/mortality_msas.csv')

    # drop all rows where notes column is total 
    mortality_data = mortality_data[mortality_data['Notes'] != 'Total']

    # keep the MSA, MSA code, and age-adjusted rate columns 
    mortality_data = mortality_data[['MSA', 'MSA Code', 'Year', 'Age-Adjusted Rate']]

    # make the MSA Code variable an integer 
    mortality_data['MSA Code'] = mortality_data['MSA Code'].astype(int)

    return mortality_data 

def load_features(dataset) -> pd.DataFrame:
    """
    Load additional features (education and income) into the dataset.
    
    Args:
        dataset (pd.DataFrame): The initial dataset containing FIPS and mortality rate.
        
    Returns:
        pd.DataFrame: The dataset enriched with features to be used for prediction.
    """
    
    # Load education data
    print('Loading race data...')
    race_data = get_race_data('2018', 'MSA', as_percent=True)
    dataset_2018 = dataset[dataset['Year'] == 2018]
    dataset_2018 = dataset_2018.merge(race_data, on='MSA Code', how='left')
    dataset = pd.concat([dataset[dataset['Year'] != 2018], dataset_2018], ignore_index=True)

    return dataset 


