from gcs_utils import get_cancer_data
from maps_utils import plot_county_choropleth, plot_disparity_chloropleth
from data_process import compute_disparity
from config import (
    MORTALITY_ALL_RACES,
    MORTALITY_HISPANIC,
    MORTALTIY_AIAN,
    MORTALITY_AAPI,
    MORTALITY_BLACK,
    MORTALITY_WHITE,
    INCIDENCE_ALL_RACES,
    INDIDENCE_HISPANIC,
    INDICDENCE_AIAN,
    INDIDENCE_AAPI,
    INDIDENCE_BLACK,
    INDIDENCE_WHITE
)

def plot_incidence_maps():
    
    # load incidence data
    incidence_all_races = get_cancer_data(INCIDENCE_ALL_RACES)
    incidence_hispanic = get_cancer_data(INDIDENCE_HISPANIC)
    incidence_aian = get_cancer_data(INDICDENCE_AIAN)
    incidence_aapi = get_cancer_data(INDIDENCE_AAPI)
    incidence_black = get_cancer_data(INDIDENCE_BLACK)
    incidence_white = get_cancer_data(INDIDENCE_WHITE)

    racial_incidence_data = [incidence_all_races, incidence_hispanic, incidence_aian, incidence_aapi, incidence_black, incidence_white]
    incidence_map_titles = ["Incidence Rate: All Races",
                            "Incidence Rate: Hispanic",
                            "Incidence Rate: American Indian/Alaskan Native",
                            "Incidence Rate: Asian/Pacific Islander",
                            "Incidence Rate: Black",
                            "Incidence Rate: White"]

    for idx, racial_data in enumerate(racial_incidence_data):
        plot_county_choropleth("maps/tl_2022_us_county.shp", 
                               racial_data, 
                               "County FIPS", 
                               "Age-Adjusted Rate per 100,000",
                               title=incidence_map_titles[idx])
        
def plot_mortality_maps():
    
    # load incidence data
    mortality_all_races = get_cancer_data(MORTALITY_ALL_RACES)
    mortality_hispanic = get_cancer_data(MORTALITY_HISPANIC)
    mortality_aian = get_cancer_data(MORTALTIY_AIAN)
    mortality_aapi = get_cancer_data(MORTALITY_AAPI)
    mortality_black = get_cancer_data(MORTALITY_BLACK)
    mortality_white = get_cancer_data(MORTALITY_WHITE)

    racial_incidence_data = [mortality_all_races, mortality_hispanic, mortality_aian, mortality_aapi, mortality_black, mortality_white]
    incidence_map_titles = ["Mortality Rate: All Races",
                            "Mortality Rate: Hispanic",
                            "Mortality Rate: American Indian/Alaskan Native",
                            "Mortality Rate: Asian American/Pacific Islander",
                            "Mortality Rate: Black",
                            "Mortality Rate: White"]

    for idx, racial_data in enumerate(racial_incidence_data):
        plot_county_choropleth("maps/tl_2022_us_county.shp", 
                               racial_data, 
                               "County FIPS", 
                               "Age-Adjusted Rate per 100,000",
                               title=incidence_map_titles[idx])

def plot_mortality_disparity_maps():

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


        
# plot_incidence_maps()
plot_mortality_maps()