from cdc_utils import get_doctors_visit_data, get_self_care_disability_data, get_frequent_mental_distress_data
from acs_utils import get_household_income_data, get_computer_data, get_grapi_data, get_language_data
from maps_utils import plot_county_choropleth
from config import SHP_FILE_PATH

def doctor_visit_map():

    # load doctor visit data
    doctor_visit_data = get_doctors_visit_data()
    
    # create chloropleth map of doctor visit rates by county
    plot_county_choropleth(SHP_FILE_PATH, doctor_visit_data, 'FIPS', 'doctor_visit_rate', 
                           title='Doctor Visit Rate by County', cmap='Blues')

def self_care_disability_map():

    # load doctor visit data
    self_care_disability_data = get_self_care_disability_data()
    
    # create chloropleth map of doctor visit rates by county
    plot_county_choropleth(SHP_FILE_PATH, self_care_disability_data, 'FIPS', 'self_care_disability_rate', 
                           title='Self Care Disability Rate by County', cmap='Blues')
    
def frequenct_mental_distress_map():

    # load doctor visit data
    frequent_mental_distress_data = get_frequent_mental_distress_data()
    
    # create chloropleth map of doctor visit rates by county
    plot_county_choropleth(SHP_FILE_PATH, frequent_mental_distress_data, 'FIPS', 'frequent_mental_distress_rate', 
                           title='Frequent Mental Distress Rate by County', cmap='Blues') 

def income_maps():
    # load household income data
    household_income_data = get_household_income_data('2022', 'county', as_percent=True)
    
    # extract columns for education levels
    data_cols = household_income_data.columns[1::]

    # Loop through each column and plot the data
    for col in data_cols:
        plot_county_choropleth(SHP_FILE_PATH,
                                household_income_data, 
                                "FIPS", 
                                col,
                                title=f"Percent of Households with income {col} by US County",
                                cmap="viridis",
                                vmin=0,
                                vmax=100)

def computer_use_maps():
    # load computer use data
    computer_use_data = get_computer_data('2022', 'county', as_percent=True)
    
    # extract columns for education levels
    data_cols = computer_use_data.columns[1::]

    for col in data_cols:
        # create chloropleth map of computer use by county
        plot_county_choropleth(SHP_FILE_PATH, 
                               computer_use_data, 
                               'FIPS',
                               col, 
                               title=f'Percent of population with {col} by US County',
                               cmap='viridis',
                               vmin=0,
                               vmax=100)

def GRAPI_maps():
    # load computer use data
    GRAPI_data = get_grapi_data('2022', 'county', as_percent=True)
    
    # extract columns for education levels
    data_cols = GRAPI_data.columns[1::]

    for col in data_cols:
        # create chloropleth map of computer use by county
        plot_county_choropleth(SHP_FILE_PATH, 
                               GRAPI_data, 
                               'FIPS',
                               col, 
                               title=f'Percent of population with rent as {col} of income by US County',
                               cmap='viridis',
                               vmin=0,
                               vmax=100)

def language_maps():
    # load language data
    language_data = get_language_data('2022', 'county', as_percent=True)
    
    # extract columns for education levels
    data_cols = language_data.columns[1::]

    for col in data_cols:
        # create chloropleth map of computer use by county
        plot_county_choropleth(SHP_FILE_PATH, 
                               language_data, 
                               'FIPS',
                               col, 
                               title=f'Percent of population speaking {col} at home by US County',
                               cmap='viridis',
                               vmin=0,
                               vmax=100)

language_maps()
