from gcs_utils import get_cancer_data
from config import MORTALITY_ALL_RACES
from acs_utils import get_education_data, get_household_income_data, get_computer_data, get_grapi_data, get_language_data 
from cdc_utils import get_doctors_visit_data, get_self_care_disability_data, get_frequent_mental_distress_data

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
    dataset = dataset.merge(education_data, on='FIPS', how='left')

    # Load household income data
    income_data = get_household_income_data('2022', 'county', as_percent=True)
    dataset = dataset.merge(income_data, on='FIPS', how='left')

    # Load computer and internet use data
    computer_data = get_computer_data('2022', 'county', as_percent=True)
    dataset = dataset.merge(computer_data, on='FIPS', how='left')

    # Load rent burden data 
    rent_burden_data = get_grapi_data('2022', 'county', as_percent=True)
    dataset = dataset.merge(rent_burden_data, on='FIPS', how='left')
    
    # Load language data 
    language_data = get_language_data('2022', 'county', as_percent=True)
    dataset = dataset.merge(language_data, on='FIPS', how='left')

    # load doctor visit data 
    doctor_visit_data = get_doctors_visit_data()
    dataset = dataset.merge(doctor_visit_data, on='FIPS', how='left')

    # load self-care disability data
    self_care_disability_data = get_self_care_disability_data()
    dataset = dataset.merge(self_care_disability_data, on='FIPS', how='left')

    # load frequency mental distress data 
    mental_distress_data = get_frequent_mental_distress_data()
    dataset = dataset.merge(mental_distress_data, on='FIPS', how='left')

    # save raw dataset to CSV 
    dataset.to_csv('dataset_raw.csv', index=False)

    return dataset