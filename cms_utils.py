import requests 
import pandas as pd 
from fedwrap.census_acs import get_total_pop

def get_all_drupal_api_items(base_url, total_pages, limit=1000):
    """
    Fetch all items from a paginated Drupal API endpoint.

    Args:
        base_url (str): The base API endpoint URL.
        total_pages (int): Total number of pages to fetch.
        limit (int): Number of items per page.

    Returns:
        list: All items from all pages.
    """
    all_items = []
    for page in range(total_pages):
        offset = page * limit 
        query_params = {}
        query_params.update({'limit': limit, 'offset': offset})
        response = requests.get(base_url, params=query_params)
        response.raise_for_status()
        data = response.json()
        all_items.extend(data)
    
    return pd.DataFrame(all_items)

def get_county_population_data():

    population_data = get_total_pop("2022","county")
    population_data['ucgid'] = population_data['ucgid'].astype(str).str[-5:]
    return population_data.rename(columns={'ucgid': 'FIPS'})

def get_medicare_data():

    # set URL to get Medicare data by county for 2022
    url = ("https://data.cms.gov/data-api/v1/dataset/d7fabe1e-d19b-4333-9eff-e80e0643f2fd/data?filter[YEAR]=2022&filter[MONTH]=Year&filter[BENE_GEO_LVL]=County")

    # query API 
    medicare_data = get_all_drupal_api_items(url,4,1000)

    # select columns of traditional medicare and medicare advantage 
    medicare_data = medicare_data.rename(columns={'BENE_FIPS_CD':'FIPS'})
    medicare_data = medicare_data[['FIPS', 'TOT_BENES', 'ORGNL_MDCR_BENES', 'MA_AND_OTH_BENES']]
    medicare_data["TOT_BENES"] = pd.to_numeric(medicare_data["TOT_BENES"], errors="coerce").astype("float64")
    medicare_data["ORGNL_MDCR_BENES"] = pd.to_numeric(medicare_data["ORGNL_MDCR_BENES"], errors="coerce").astype("float64")
    medicare_data["MA_AND_OTH_BENES"] = pd.to_numeric(medicare_data["MA_AND_OTH_BENES"], errors="coerce").astype("float64")

    # get population by county for 2022
    population_data = get_county_population_data()

    # merge medicare data with population data 
    population_data = population_data.merge(medicare_data, on='FIPS', how='left')

    # divide to get percent of population on TM and MA
    population_data["total_medicare_percent"] = (
        population_data["TOT_BENES"] / population_data["Total population"] * 100
    ).round(1)
    population_data["original_medicare_percent"] = (
        population_data["ORGNL_MDCR_BENES"] / population_data["Total population"] * 100
    ).round(1)
    population_data["medicare_advantage_percent"] = (
        population_data["MA_AND_OTH_BENES"] / population_data["Total population"] * 100
    ).round(1)

    # Drop columns and return 
    return population_data.drop(columns=['Total population', 'TOT_BENES', 'ORGNL_MDCR_BENES', 'MA_AND_OTH_BENES'])

def clean_marketplace_data():

    marketplace_data = pd.read_csv("data/marketplace_enrollment_2022.csv")

    # convert FIPS to string and pad 0s 
    marketplace_data['County_FIPS_Cd'] = marketplace_data['County_FIPS_Cd'].astype(str).str.zfill(5)

    # convert enrollees to float64
    marketplace_data['Cnsmr'] = marketplace_data['Cnsmr'].str.replace(',', '', regex=False)
    marketplace_data['Cnsmr'] = pd.to_numeric(marketplace_data["Cnsmr"], errors="coerce").astype("float64")

    # rename columns
    marketplace_data = marketplace_data.rename(columns={'County_FIPS_Cd':'FIPS'})
    marketplace_data = marketplace_data.rename(columns={'Cnsmr':'marketplace_enrollees'})

    # keep relevant columns 
    return marketplace_data[['FIPS', 'marketplace_enrollees']]

def get_marketplace_data():

    # get marketplace data 
    marketplace_data = clean_marketplace_data()

    # get population by county for 2022
    population_data = get_county_population_data()

    # merge
    population_data = population_data.merge(marketplace_data, on='FIPS', how='left')

    # divide to get percent of population on TM and MA
    population_data["marketplace_percent"] = (
        population_data["marketplace_enrollees"] / population_data["Total population"] * 100
    ).round(1)


    return population_data[['FIPS','marketplace_percent']]

