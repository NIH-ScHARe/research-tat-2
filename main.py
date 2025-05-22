from gcs_utils import get_cancer_data
from config import MORTALITY_ALL_RACES
from acs_utils import get_education_data, get_household_income_data


if __name__ == "__main__":

    # Load cancer data
    mortality_all_races = get_cancer_data(MORTALITY_ALL_RACES)
    
    education_data = get_education_data('2022', 'county', as_percent=True)
    income_data = get_household_income_data('2022', 'county', as_percent=True)


    

