from maps_utils import plot_county_choropleth
from acs_utils import get_education_data
from config import SHP_FILE_PATH

def chloropleth_each_education_level(education_data, data_cols):

    # Loop through each column and plot the data
    for col in data_cols:
        plot_county_choropleth(SHP_FILE_PATH,
                                education_data, 
                                "FIPS", 
                                col,
                                title=f"Percent of Population with {col} by US County",
                                cmap="viridis",
                                vmin=0,
                                vmax=100)

def chloropleth_cummulative_education(education_data, data_cols):

    # create a new dataframe to hold the cumulative percent data
    cummulative_education = education_data[["FIPS"]].copy()    

    # loop through each education level, calculate the cumulative percent, and plot 
    for i, col in enumerate(reversed(data_cols)):
        # calculate cumulative percent
        if i == 0:
            cummulative_education["Cumulative Percent"] = education_data[col]
        else:
            cummulative_education["Cumulative Percent"] += education_data[col]
        
        # plot the data
        plot_county_choropleth("maps/tl_2022_us_county.shp",
                                cummulative_education, 
                                "FIPS", 
                                "Cumulative Percent",
                                title=f"Percent of Population with at least a {col} by US County",
                                cmap="viridis",
                                vmin=0,
                                vmax=100)

# fetch education data 
education_data = get_education_data('2022', 'county', as_percent=True)

# extract columns for education levels
data_cols = education_data.columns[1:-1]

# create chloropleths 
chloropleth_each_education_level(education_data, data_cols)
chloropleth_cummulative_education(education_data, data_cols)
