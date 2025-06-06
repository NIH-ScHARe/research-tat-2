import pandas as pd 
from fedwrap.cdc_places import get_places_data 

def clean_places_data(df, column_name):

    # keep only relevant columns
    df = df[['locationid', 'data_value']].copy()

    # make data value column numeric 
    df['data_value'] = pd.to_numeric(df['data_value'], errors='coerce')

    # rename columns for clarity
    df = df.rename(columns={'locationid': 'FIPS', 'data_value': column_name})
    
    return df

def fetch_places_data(geo,year,datavalueid,datatypeid):

    # fetch dataset 
    data = get_places_data(geo, year, datavalueid, datatypeid)

    # clean dataset and label column based on datavalueid
    if datavalueid == 'CHECKUP':
        return clean_places_data(data, 'doctor_visit_rate')
    elif datavalueid == 'SELFCARE':
        return clean_places_data(data, 'self_care_disability_rate')
    elif datavalueid == 'MHLTH':
        return clean_places_data(data, 'frequent_mental_distress_rate')
    elif datavalueid == 'ACCESS2':
        return clean_places_data(data, 'health_insurance_access_rate')
    elif datavalueid == 'INDEPLIVE':
        return clean_places_data(data, 'independent_living_disability_rate')
    elif datavalueid == 'ISOLATION':
        return clean_places_data(data, 'social_isolation_rate')
    elif datavalueid == 'FOODINSECU':
        return clean_places_data(data, 'food_insecurity_rate')
    elif datavalueid == 'HOUSINSECU':
        return clean_places_data(data, 'housing_insecurity_rate')
    elif datavalueid == 'LACKTRPT':
        return clean_places_data(data, 'lack_reliable_transportation_rate')
    elif datavalueid == 'EMOTIONSPT':
        return clean_places_data(data, 'lack_emotional_support_rate')
    else:
        raise ValueError(f"Unsupported datavalueid: {datavalueid}")
    