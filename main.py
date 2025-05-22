from gcs_utils import get_cancer_data
from mapping import plot_county_choropleth, plot_disparity_chloropleth
from config import MORTALITY_ALL_RACES
from acs_utils import get_education_data


if __name__ == "__main__":

    # Load cancer data
    mortality_all_races = get_cancer_data(MORTALITY_ALL_RACES)
    
    education_data = get_education_data('2022', 'county', as_percent=True)

    

