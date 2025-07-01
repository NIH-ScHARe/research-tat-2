from gcs_utils import get_cancer_data
from config import MORTALITY_ALL_RACES
from acs_utils import get_education_data, get_household_income_data, get_computer_data, get_grapi_data, get_language_data, get_private_insurance_data, get_public_insurance_data
from cdc_utils import fetch_places_data
from cms_utils import get_medicare_data, get_marketplace_data, get_dual_enrollee_data

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
        pd.DataFrame: The dataset enriched with features to be used for prediction.
    """
    
    # Load education data
    print('Loading education data...')
    education_data = get_education_data('2022', 'county', as_percent=True)
    dataset = dataset.merge(education_data, on='FIPS', how='left')

    # Load household income data
    print('Loading household income data...')
    income_data = get_household_income_data('2022', 'county', as_percent=True)
    dataset = dataset.merge(income_data, on='FIPS', how='left')

    # Load computer and internet use data
    print('Loading computer and internet use data...')
    computer_data = get_computer_data('2022', 'county', as_percent=True)
    dataset = dataset.merge(computer_data, on='FIPS', how='left')

    # Load rent burden data 
    print('Loading rent burden data...')
    rent_burden_data = get_grapi_data('2022', 'county', as_percent=True)
    dataset = dataset.merge(rent_burden_data, on='FIPS', how='left')
    
    # Load language data 
    print('Loading language data...')
    language_data = get_language_data('2022', 'county', as_percent=True)
    dataset = dataset.merge(language_data, on='FIPS', how='left')

    # load doctor visit data 
    print('Loading doctor visit data...')
    doctor_visit_data = fetch_places_data('county', '2022', 'CHECKUP', 'AgeAdjPrv')
    dataset = dataset.merge(doctor_visit_data, on='FIPS', how='left')

    # load self-care disability data
    print('Loading self-care disability data...')
    self_care_disability_data = fetch_places_data('county', '2022', 'SELFCARE', 'AgeAdjPrv')
    dataset = dataset.merge(self_care_disability_data, on='FIPS', how='left')

    # load frequency mental distress data 
    print('Loading frequent mental distress data...')
    mental_distress_data = fetch_places_data('county', '2022', 'MHLTH', 'AgeAdjPrv')
    dataset = dataset.merge(mental_distress_data, on='FIPS', how='left')

    # load health insurance access data 
    print('Loading health insurance access data...')
    health_insurance_data = fetch_places_data('county', '2022', 'ACCESS2', 'AgeAdjPrv')
    dataset = dataset.merge(health_insurance_data, on='FIPS', how='left')

    # load independent living disability data
    print('Loading independent living disability data...')
    independent_living_data = fetch_places_data('county', '2022', 'INDEPLIVE', 'AgeAdjPrv')    
    dataset = dataset.merge(independent_living_data, on='FIPS', how='left')

    # load social isolation data
    print('Loading social isolation data...')
    social_isolation_data = fetch_places_data('county', '2022', 'ISOLATION', 'AgeAdjPrv')
    dataset = dataset.merge(social_isolation_data, on='FIPS', how='left')

    # load food insecurity data
    print('Loading food insecurity data...')
    food_insecurity_data = fetch_places_data('county', '2022', 'FOODINSECU', 'AgeAdjPrv')
    dataset = dataset.merge(food_insecurity_data, on='FIPS', how='left')

    # load housing insecurity data
    print('Loading housing insecurity data...')
    housing_insecurity_data = fetch_places_data('county', '2022', 'HOUSINSECU', 'AgeAdjPrv')
    dataset = dataset.merge(housing_insecurity_data, on='FIPS', how='left')

    # load lack of reliable transportation data
    print('Loading lack of reliable transportation data...')
    lack_transportation_data = fetch_places_data('county', '2022', 'LACKTRPT', 'AgeAdjPrv')    
    dataset = dataset.merge(lack_transportation_data, on='FIPS', how='left')

    # load lack of emotional support data
    print('Loading lack of emotional support data...')
    lack_emotional_support_data = fetch_places_data('county', '2022', 'EMOTIONSPT', 'AgeAdjPrv')
    dataset = dataset.merge(lack_emotional_support_data, on='FIPS', how='left')

    # load Medicare data 
    print('Loading Medicare data...')
    medicare_data = get_medicare_data()
    dataset = dataset.merge(medicare_data, on='FIPS', how='left')

    # load marketplace data 
    print('Loading marketplace data...')
    marketplace_data = get_marketplace_data()
    dataset = dataset.merge(marketplace_data, on='FIPS', how='left')

    # load dual enrollee data 
    print('Loading dual enrollee data...')
    dual_enrollee_data = get_dual_enrollee_data()
    dataset = dataset.merge(dual_enrollee_data, on='FIPS', how='left')

    # load private insurance data
    print('Loading private insurance data...')
    private_insurance_data = get_private_insurance_data()
    dataset = dataset.merge(private_insurance_data, on='FIPS', how='left')

    # load public insurance data 
    print('Loading public insurance data...')
    public_insurance_data = get_public_insurance_data()
    dataset = dataset.merge(public_insurance_data, on='FIPS', how='left')

    # save raw dataset to CSV 
    dataset.to_csv('dataset_raw.csv', index=False)

    return dataset