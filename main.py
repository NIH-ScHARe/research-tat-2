from gcs_utils import get_cancer_data
from mapping import plot_county_choropleth, plot_disparity_chloropleth
from config import MORTALITY_ALL_RACES, MORTALITY_HISPANIC, MORTALTIY_AIAN, MORTALITY_AAPI, MORTALITY_BLACK, MORTALITY_WHITE
from data_process import compute_disparity

if __name__ == "__main__":

    # Load cancer data
    mortality_all_races = get_cancer_data(MORTALITY_ALL_RACES)
    mortality_hispanic = get_cancer_data(MORTALITY_HISPANIC)
    mortality_aian = get_cancer_data(MORTALTIY_AIAN)
    mortality_aapi = get_cancer_data(MORTALITY_AAPI)
    mortality_black = get_cancer_data(MORTALITY_BLACK)
    mortality_white = get_cancer_data(MORTALITY_WHITE)

    # Compute disparity
    disparity_hispanic = compute_disparity(mortality_all_races, mortality_hispanic)

    # plot_county_choropleth("maps/tl_2022_us_county.shp", mortality_black, "County FIPS", "Age-Adjusted Rate per 100,000")

    # Plot the disparity
    plot_disparity_chloropleth("maps/tl_2022_us_county.shp", disparity_hispanic, "County FIPS", "mortality_rate_disparity")
    