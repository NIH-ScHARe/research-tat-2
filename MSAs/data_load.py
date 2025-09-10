import pandas as pd 
from acs_utils import get_race_data, get_education_data

def load_mortality_data() -> pd.DataFrame:
    """
    Load the mortality rate data from the CDC WONDER database and preprocess it. 
    
    Returns:
        MortalityDataFrameModel: A model containing the MSA, MSA code, year, and age-adjusted mortality rate DataFrame.
    """

    # load mortality data from the csv file 
    mortality_data = pd.read_csv('data/mortality_msas.csv')

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

def load_features(dataset) -> pd.DataFrame:
    """
    Load additional features (education and income) into the dataset.
    
    Args:
        dataset (pd.DataFrame): The initial dataset containing FIPS and mortality rate.
        
    Returns:
        pd.DataFrame: The dataset enriched with features to be used for prediction.
    """
    
    # # Load racial data
    # for year in dataset['Year'].unique():
    #     print(f'Loading racial data for the year {year}...') 

    #     race_data = get_race_data(str(year), 'MSA', as_percent=True)
    
    #     # add column for year as int64
    #     race_data['Year'] = pd.Series(year, index=race_data.index, dtype='int64')

    #     # merge to the full dataset on year and MSA code 
    #     dataset = pd.merge(dataset, race_data, on=["MSA Code", "Year"], how='left')

    # return dataset 

    # Load education data
    all_year_data = []
    for year in dataset['year'].unique():
        print(f'Loading education data for the year {year}...') 

        year_data = get_education_data(str(year), 'MSA', as_percent=True)
    
        # add column for year as int64
        year_data['year'] = pd.Series(year, index=year_data.index, dtype='int64')

        all_year_data.append(year_data)

    education_data = pd.concat(all_year_data, ignore_index=True)

    # merge to the full dataset on year and MSA code 
    dataset = pd.merge(dataset, education_data, on=["msa_code", "year"], how='left')

    return dataset

