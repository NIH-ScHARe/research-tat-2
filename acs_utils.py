import sys, os

# Add the SCHARE-tools directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'SCHARE-tools')))

from census_acs import get_educational_attainment

def get_education_data(year, geography, as_percent=False):
    """
    Fetches educational attainment data from the ACS for a given year and geography.
    
    Args:
        year (str): The year of the ACS data to fetch.
        geography (str): The type of geography to fetch data for (e.g., 'county').
        as_percent (bool): If True, returns the data as percentages. Defaults to False.
    
    Returns:
        pd.DataFrame: A DataFrame containing the educational attainment data.
    """
    # Fetch the educational attainment data
    education_data = get_educational_attainment(year, geography, as_percent=as_percent)
    
    # Cleans the FIPS code by taking the last 5 characters of the ucgid column 
    education_data['FIPS'] = education_data['ucgid'].astype(str).str[-5:]

    return education_data