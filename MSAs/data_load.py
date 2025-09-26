import pandas as pd 
from fedwrap.census_acs import get_educational_attainment, get_household_income, get_language_spoken_at_home
from acs_utils import get_private_insurance_data, get_public_insurance_data

def load_mortality_data() -> pd.DataFrame:
    """
    Load the mortality rate data from the CDC WONDER database and preprocess it. 
    
    Returns:
        MortalityDataFrameModel: A model containing the MSA, MSA code, year, and age-adjusted mortality rate DataFrame.
    """

    # load mortality data from the csv file 
    mortality_data = pd.read_csv('MSAs/data/mortality_msas.csv')

    # drop all rows where notes column is total 
    mortality_data = mortality_data[mortality_data['Notes'] != 'Total']

    # keep the MSA, MSA code, and age-adjusted rate columns 
    mortality_data = mortality_data[['MSA', 'MSA Code', 'Year', 'Age-Adjusted Rate']]

    # drop empty rows 
    mortality_data = mortality_data.dropna()

    # make the MSA Code variable an integer 
    mortality_data['MSA Code'] = mortality_data['MSA Code'].astype(int)

    # make the year variable an integer 
    mortality_data['Year'] = mortality_data['Year'].astype(int)

    # drop the rows where the MSA Code is 99999
    mortality_data = mortality_data[mortality_data['MSA Code'] != 99999]

    # rename columns 
    mortality_data = mortality_data.rename(columns={
        'MSA': 'msa_text',
        'MSA Code': 'msa_code',
        'Year': 'year',
        'Age-Adjusted Rate': 'mortality_rate'
    })

    return mortality_data 

def get_data_over_years(
        dataset: pd.DataFrame, 
        fetch_fn,
        year_col: str = "year",
):
    
    years = pd.Index(dataset[year_col].unique()).astype(str)
    frames = [] 

    for year in years:
        print(f'Using function {str(fetch_fn)} and loading data for the year {year}...') 

        # Fetch data from the ACS API
        year_data = fetch_fn(year, 'MSA', as_percent=True)
        
        # Replace the ucgid column with its last 5 characters (FIPS code) and rename to FIPS
        year_data['ucgid'] = year_data['ucgid'].astype(str).str[-5:].astype(int)
        year_data = year_data.rename(columns={'ucgid': 'msa_code'})

        # add column for year as int64
        year_data[year_col] = int(year)

        frames.append(year_data)

    education_data = pd.concat(frames, ignore_index=True)

    return pd.merge(dataset, education_data, on=["msa_code", "year"], how='left') 
    

def load_features(dataset) -> pd.DataFrame:
    """
    Load additional features (education and income) into the dataset.
    
    Args:
        dataset (pd.DataFrame): The initial dataset containing FIPS and mortality rate.
        
    Returns:
        pd.DataFrame: The dataset enriched with features to be used for prediction.
    """
    
    fetch_fns = [
        get_educational_attainment,
        get_household_income,
        get_language_spoken_at_home,
        get_private_insurance_data,
        get_public_insurance_data
    ]

    for fetch_fn in fetch_fns:
        dataset = get_data_over_years(dataset, fetch_fn)

    return dataset 

def load_data():
    data = load_mortality_data()
    data = load_features(data)
    data.to_csv('MSAs/data/data_00_raw.csv', index=False)