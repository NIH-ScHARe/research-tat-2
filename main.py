from gcs_utils import get_cancer_data
from mapping import plot_county_choropleth
from config import MORTALITY_ALL_RACES, MORTALITY_HISPANIC, MORTALTIY_AIAN, MORTALITY_AAPI, MORTALITY_BLACK, MORTALITY_WHITE

if __name__ == "__main__":

    # Load cancer data
    mortality_all_races = get_cancer_data(MORTALITY_ALL_RACES)
    mortality_hispanic = get_cancer_data(MORTALITY_HISPANIC)
    mortality_aian = get_cancer_data(MORTALTIY_AIAN)
    mortality_aapi = get_cancer_data(MORTALITY_AAPI)
    mortality_black = get_cancer_data(MORTALITY_BLACK)
    mortality_white = get_cancer_data(MORTALITY_WHITE)

    plot_county_choropleth("maps/tl_2022_us_county.shp", mortality_black, "County FIPS", "Age-Adjusted Rate per 100,000")

    