from gcs_utils import get_cancer_data
from mapping import plot_county_choropleth, plot_disparity_chloropleth
from config import MORTALITY_ALL_RACES, MORTALITY_HISPANIC, MORTALTIY_AIAN, MORTALITY_AAPI, MORTALITY_BLACK, MORTALITY_WHITE
from data_process import compute_disparity


# Load cancer data
mortality_all_races = get_cancer_data(MORTALITY_ALL_RACES)
mortality_hispanic = get_cancer_data(MORTALITY_HISPANIC)
mortality_aian = get_cancer_data(MORTALTIY_AIAN)
mortality_aapi = get_cancer_data(MORTALITY_AAPI)
mortality_black = get_cancer_data(MORTALITY_BLACK)
mortality_white = get_cancer_data(MORTALITY_WHITE)

racial_mortality_data = [mortality_hispanic, mortality_aian, mortality_aapi, mortality_black, mortality_white]
disparity_map_titles = ["Mortality Disparity: Hispanic compared to All Races",
                        "Mortality Disparity: American Indian/Alaskan Native compared to all races",
                        "Mortality Disparity: Asian/Pacific Islander compared to all races",
                        "Mortality Disparity: Black compared to all races",
                        "Mortality Disparity: White compared to all races"]

for idx, racial_data in enumerate(racial_mortality_data):

    disparity_data = compute_disparity(mortality_all_races, racial_data)
    plot_disparity_chloropleth("maps/tl_2022_us_county.shp", 
                                disparity_data, 
                                "County FIPS", 
                                "mortality_rate_disparity",
                                title=disparity_map_titles[idx])
