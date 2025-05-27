import requests
import pandas as pd

def query_places_api(api_endpoint,column_name):
    """
    Queries the CDC Places API with a given SQL query and returns the results as a DataFrame.
    
    Args:
        query (str): The SQL query to execute on the CDC Places API.
        column_name (str): The name of the column to rename the results to. 
        
    Returns:
        pd.DataFrame: A DataFrame containing the results of the query.
    """
    
    # retrieve data and convert to DataFrame
    response = requests.get(api_endpoint)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        
        # keep only relevant columns
        df = df[['locationid', 'data_value']]

        # rename columns for clarity
        df = df.rename(columns={'locationid': 'FIPS', 'data_value': column_name})
        
        return df
    else:
        raise Exception(f"Failed to retrieve data: {response.status_code} - {response.text}")

def get_doctors_visit_data():

    api_endpoint = 'https://data.cdc.gov/resource/swc5-untb.json?$query=SELECT%0A%20%20%60year%60%2C%0A%20%20%60stateabbr%60%2C%0A%20%20%60statedesc%60%2C%0A%20%20%60locationname%60%2C%0A%20%20%60datasource%60%2C%0A%20%20%60category%60%2C%0A%20%20%60measure%60%2C%0A%20%20%60data_value_unit%60%2C%0A%20%20%60data_value_type%60%2C%0A%20%20%60data_value%60%2C%0A%20%20%60data_value_footnote_symbol%60%2C%0A%20%20%60data_value_footnote%60%2C%0A%20%20%60low_confidence_limit%60%2C%0A%20%20%60high_confidence_limit%60%2C%0A%20%20%60totalpopulation%60%2C%0A%20%20%60totalpop18plus%60%2C%0A%20%20%60locationid%60%2C%0A%20%20%60categoryid%60%2C%0A%20%20%60measureid%60%2C%0A%20%20%60datavaluetypeid%60%2C%0A%20%20%60short_question_text%60%2C%0A%20%20%60geolocation%60%0AWHERE%0A%20%20caseless_eq(%60year%60%2C%20%222022%22)%0A%20%20AND%20caseless_one_of(%0A%20%20%20%20%60measure%60%2C%0A%20%20%20%20%22Visits%20to%20doctor%20for%20routine%20checkup%20within%20the%20past%20year%20among%20adults%22%0A%20%20)%0A%20%20AND%20caseless_one_of(%60data_value_type%60%2C%20%22Age-adjusted%20prevalence%22)'

    return query_places_api(api_endpoint, 'doctor_visit_rate')


def get_self_care_disability_data():

    api_endpoint = 'https://data.cdc.gov/resource/swc5-untb.json?$query=SELECT%0A%20%20%60year%60%2C%0A%20%20%60stateabbr%60%2C%0A%20%20%60statedesc%60%2C%0A%20%20%60locationname%60%2C%0A%20%20%60datasource%60%2C%0A%20%20%60category%60%2C%0A%20%20%60measure%60%2C%0A%20%20%60data_value_unit%60%2C%0A%20%20%60data_value_type%60%2C%0A%20%20%60data_value%60%2C%0A%20%20%60data_value_footnote_symbol%60%2C%0A%20%20%60data_value_footnote%60%2C%0A%20%20%60low_confidence_limit%60%2C%0A%20%20%60high_confidence_limit%60%2C%0A%20%20%60totalpopulation%60%2C%0A%20%20%60totalpop18plus%60%2C%0A%20%20%60locationid%60%2C%0A%20%20%60categoryid%60%2C%0A%20%20%60measureid%60%2C%0A%20%20%60datavaluetypeid%60%2C%0A%20%20%60short_question_text%60%2C%0A%20%20%60geolocation%60%0AWHERE%0A%20%20caseless_eq(%60year%60%2C%20%222022%22)%0A%20%20AND%20caseless_one_of(%60measure%60%2C%20%22Self-care%20disability%20among%20adults%22)%0A%20%20AND%20caseless_one_of(%60data_value_type%60%2C%20%22Age-adjusted%20prevalence%22)'

    return query_places_api(api_endpoint, 'self_care_disability_rate')

def get_frequent_mental_distress_data():

    api_endpoint = 'https://data.cdc.gov/resource/swc5-untb.json?$query=SELECT%0A%20%20%60year%60%2C%0A%20%20%60stateabbr%60%2C%0A%20%20%60statedesc%60%2C%0A%20%20%60locationname%60%2C%0A%20%20%60datasource%60%2C%0A%20%20%60category%60%2C%0A%20%20%60measure%60%2C%0A%20%20%60data_value_unit%60%2C%0A%20%20%60data_value_type%60%2C%0A%20%20%60data_value%60%2C%0A%20%20%60data_value_footnote_symbol%60%2C%0A%20%20%60data_value_footnote%60%2C%0A%20%20%60low_confidence_limit%60%2C%0A%20%20%60high_confidence_limit%60%2C%0A%20%20%60totalpopulation%60%2C%0A%20%20%60totalpop18plus%60%2C%0A%20%20%60locationid%60%2C%0A%20%20%60categoryid%60%2C%0A%20%20%60measureid%60%2C%0A%20%20%60datavaluetypeid%60%2C%0A%20%20%60short_question_text%60%2C%0A%20%20%60geolocation%60%0AWHERE%0A%20%20caseless_eq(%60year%60%2C%20%222022%22)%0A%20%20AND%20caseless_one_of(%0A%20%20%20%20%60measure%60%2C%0A%20%20%20%20%22Frequent%20mental%20distress%20among%20adults%22%0A%20%20)%0A%20%20AND%20caseless_one_of(%60data_value_type%60%2C%20%22Age-adjusted%20prevalence%22)'

    return query_places_api(api_endpoint, 'frequent_mental_distress_rate')