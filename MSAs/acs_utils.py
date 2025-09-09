from fedwrap.census_acs import get_race 


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
    race_data['ucgid'] = race_data['ucgid'].astype(str).str[-5:]
    race_data = race_data.rename(columns={'ucgid': 'MSA Code'})

    return race_data