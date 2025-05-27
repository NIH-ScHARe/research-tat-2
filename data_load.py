from acs_utils import get_education_data, get_household_income_data
from gcs_utils import get_cancer_data
from config import MORTALITY_ALL_RACES

def load_target():

    # Load cancer mortality rate data
    mortality_all_races = get_cancer_data(MORTALITY_ALL_RACES)
    
    # isolate columns for analysis 
    dataset = mortality_all_races[['FIPS','mortality_rate']]

    return dataset 

def load_features(dataset):
    """
    Load additional features (education and income) into the dataset.
    
    Args:
        dataset (pd.DataFrame): The initial dataset containing FIPS and mortality rate.
        
    Returns:
        pd.DataFrame: The dataset enriched with education and income features.
    """
    
    # Load education data
    education_data = get_education_data('2022', 'county', as_percent=True)
    
    # Load household income data
    income_data = get_household_income_data('2022', 'county', as_percent=True)
    
    # Merge education and income data into the main dataset
    dataset = dataset.merge(education_data, on='FIPS', how='left')
    dataset = dataset.merge(income_data, on='FIPS', how='left')
    
    # save raw dataset to CSV 
    dataset.to_csv('dataset_raw.csv', index=False)

    return dataset