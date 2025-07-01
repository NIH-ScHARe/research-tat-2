import pandas as pd 
from fedwrap.census_acs import get_educational_attainment, get_household_income, get_computer_and_internet_use, get_GRAPI, get_language_spoken_at_home
import requests 

def get_language_data(year, geography, as_percent=False):
    """
    Fetches the language spoken at home data from the ACS for a given year and geography.
    Args:
        year (str): The year of the ACS data to fetch.
        geography (str): The type of geography to fetch data for (e.g., 'county').
        as_percent (bool): If True, returns the data as percentages. Defaults to False. 
    
    Returns:
        pd.DataFrame: A DataFrame containing the language spoken at home data.
    """
    # Fetch the language spoken at home data
    language_data = get_language_spoken_at_home(year, geography, as_percent=as_percent)
    
    # Cleans the FIPS code by taking the last 5 characters of the ucgid column 
    language_data['ucgid'] = language_data['ucgid'].astype(str).str[-5:]
    language_data = language_data.rename(columns={'ucgid': 'FIPS'})

    return language_data

def get_grapi_data(year, geography, as_percent=False):
    """
    Fetches the Gross Rent as a Percentage of Income (GRAPI) data from the ACS for a given year and geography.
    Args:
        year (str): The year of the ACS data to fetch.
        geography (str): The type of geography to fetch data for (e.g., 'county').
        as_percent (bool): If True, returns the data as percentages. Defaults to False.
    Returns:
        pd.DataFrame: A DataFrame containing the GRAPI data.
    """

    # Fetch the GRAPI data
    grapi_data = get_GRAPI(year, geography, as_percent=as_percent)
    
    # Cleans the FIPS code by taking the last 5 characters of the ucgid column 
    grapi_data['ucgid'] = grapi_data['ucgid'].astype(str).str[-5:]
    grapi_data = grapi_data.rename(columns={'ucgid': 'FIPS'})

    # convert the other columns to numeric 
    for col in grapi_data.columns[1:]:
        grapi_data[col] = pd.to_numeric(grapi_data[col], errors='coerce')
        grapi_data.loc[grapi_data[col] < 0, col] = pd.NA

    
    return grapi_data

def get_computer_data(year, geography, as_percent=False):
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
    computer_data = get_computer_and_internet_use(year, geography, as_percent=as_percent)
    
    # Cleans the FIPS code by taking the last 5 characters of the ucgid column 
    computer_data['ucgid'] = computer_data['ucgid'].astype(str).str[-5:]
    computer_data = computer_data.rename(columns={'ucgid': 'FIPS'})

    return computer_data

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
    education_data['ucgid'] = education_data['ucgid'].astype(str).str[-5:]
    education_data = education_data.rename(columns={'ucgid': 'FIPS'})

    return education_data

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
    income_data['ucgid'] = income_data['ucgid'].astype(str).str[-5:]
    income_data = income_data.rename(columns={'ucgid': 'FIPS'})

    return income_data

def get_private_insurance_data():
    
    url = 'https://api.census.gov/data/2022/acs/acs5/subject?get=group(S2703)&ucgid=pseudo(0100000US$0500000)'

    table = requests.get(url)

    df = pd.DataFrame(table.json())
    
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)

    data = df[['ucgid','S2703_C01_002E','S2703_C03_006E','S2703_C03_010E']].copy()

    data['ucgid'] = data['ucgid'].astype(str).str[-5:]
    data = data.rename(columns={'ucgid': 'FIPS','S2703_C01_002E': 'Employer-based health insurance alone or in combination',
                                'S2703_C03_006E': 'Direct-purchase health insurance alone or in combination',
                                'S2703_C03_010E': 'Tricare/military health insurance alone or in combination'})

    return data

def get_public_insurance_data():

    url = 'https://api.census.gov/data/2022/acs/acs5/subject?get=group(S2704)&ucgid=pseudo(0100000US$0500000)'

    table = requests.get(url)

    df = pd.DataFrame(table.json())
    
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)

    data = df[['ucgid','S2704_C03_002E','S2704_C03_006E','S2704_C03_010E']].copy()

    data['ucgid'] = data['ucgid'].astype(str).str[-5:]
    data = data.rename(columns={'ucgid': 'FIPS',
                                'S2704_C03_002E': 'Medicare coverage alone or in combination',
                                'S2704_C03_006E': 'Medicaid/means-tested public coverage alone or in combination',
                                'S2704_C03_010E': 'VA health care coverage alone or in combination'})

    return data