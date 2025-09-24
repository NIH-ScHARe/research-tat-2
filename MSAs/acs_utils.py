from fedwrap.census_acs import get_race, get_educational_attainment, get_household_income
import requests
import pandas as pd 

def get_race_data(year, geography, as_percent=False):
    """
        Fetches race data from the ACS for a given year and geography.
        
        Args:
            year (str): The year of the ACS data to fetch.
            geography (str): The type of geography to fetch data for (e.g., 'county').
            as_percent (bool): If True, returns the data as percentages. Defaults to False.
        
        Returns:
            pd.DataFrame: A DataFrame containing the educational attainment data.
        """
    # Fetch the educational attainment data
    race_data = get_race(year, geography, as_percent=as_percent)
    
    # Replace the ucgid column with its last 5 characters (FIPS code) and rename to FIPS
    race_data['ucgid'] = race_data['ucgid'].astype(str).str[-5:].astype(int)
    race_data = race_data.rename(columns={'ucgid': 'msa_code'})

    return race_data



def get_education_data(year, geography, as_percent=False):
    """
        Fetches race data from the ACS for a given year and geography.
        
        Args:
            year (str): The year of the ACS data to fetch.
            geography (str): The type of geography to fetch data for (e.g., 'county').
            as_percent (bool): If True, returns the data as percentages. Defaults to False.
        
        Returns:
            pd.DataFrame: A DataFrame containing the educational attainment data.
        """
    # Fetch the educational attainment data
    data = get_educational_attainment(year, geography, as_percent=as_percent)
    
    # Replace the ucgid column with its last 5 characters (FIPS code) and rename to FIPS
    data['ucgid'] = data['ucgid'].astype(str).str[-5:].astype(int)
    data = data.rename(columns={'ucgid': 'msa_code'})

    return data

def get_household_income_data(year, geography, as_percent=False):
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
    income_data = get_household_income(year, geography, as_percent=as_percent)
    
    # Replace the ucgid column with its last 5 characters (FIPS code) and rename to FIPS
    income_data['ucgid'] = income_data['ucgid'].astype(str).str[-5:].astype(int)
    income_data = income_data.rename(columns={'ucgid': 'msa_code'})

    return income_data

def get_private_insurance_data(year: str, geography, as_percent=False) -> pd.DataFrame:
    
    url = 'https://api.census.gov/data/' + year + '/acs/acs5/subject?get=group(S2703)&ucgid=pseudo(0100000US$31000M1)'

    table = requests.get(url)

    df = pd.DataFrame(table.json())
    
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)

    data = df[['ucgid','S2703_C03_002E','S2703_C03_006E','S2703_C03_010E']].copy()

    data = data.rename(columns={'S2703_C03_002E': 'employer_based_health_insurance',
                                'S2703_C03_006E': 'direct_purchase_health_insurance',
                                'S2703_C03_010E': 'tricare_health_insurance'})

    return data

