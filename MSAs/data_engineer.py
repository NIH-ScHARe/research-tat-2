import pandas as pd 

def engineer_data():
    
    # load clean data 
    data = pd.read_csv('MSAs/data/data_01_clean.csv')
    
    # center years for interpretable intercepts 
    data["year_centered"] = data["year"] - 2018
    
    # create education level categories 
    data["less_than_hs"] = round(data["Less than 9th grade"] + data["9th to 12th grade, no diploma"],1)
    data["hs"] = round(data["High school graduate (includes equivalency)"] + data["Some college, no degree"] + data["Associate's degree"],1)
    data["college_plus"] = round(data["Bachelor's degree"] + data["Graduate or professional degree"],1)
    
    # create income categories 
    data['low_income'] = round(data["Less than $10,000"] +
                             data["$10,000 to $14,999"] +
                             data["$15,000 to $24,999"] +
                             data["$25,000 to $34,999"],1)
    data['middle_income'] = round(data["$35,000 to $49,999"] +
                             data["$50,000 to $74,999"] +
                             data["$75,000 to $99,999"],1)
    data['high_income'] = round(data["$100,000 to $149,999"] +
                                    data["$150,000 to $199,999"] +
                                    data["$200,000 or more"],1)

    # save engineered data to file 
    data.to_csv('MSAs/data/data_02_engineered.csv', index=False)