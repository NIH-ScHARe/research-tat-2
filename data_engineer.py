def engineer_education(data,drop):
    data['complete_high_school'] = (data['High school graduate (includes equivalency)'] + 
                                        data['Some college, no degree'] + 
                                        data['Associate\'s degree'] + 
                                        data['Bachelor\'s degree'] + 
                                        data['Graduate or professional degree'])
    data['attend_college'] = (data['Some college, no degree'] + 
                                        data['Associate\'s degree'] + 
                                        data['Bachelor\'s degree'] + 
                                        data['Graduate or professional degree'])
    data['complete_college'] = (data['Associate\'s degree'] + 
                                        data['Bachelor\'s degree'] + 
                                        data['Graduate or professional degree'])
    data['advanced_degree'] = data['Graduate or professional degree']
    
    if drop:
        data.drop(columns=['Less than 9th grade',
                    '9th to 12th grade, no diploma',
                    'High school graduate (includes equivalency)',
                    'Some college, no degree',
                    'Associate\'s degree',
                    'Bachelor\'s degree',
                    'Graduate or professional degree'],inplace=True)

    return data 

def engineer_income(data,drop):

    """
    Engineer income-related features in the DataFrame.
    
    Args:
        data (pd.DataFrame): The DataFrame containing income data.
        
    Returns:
        pd.DataFrame: The DataFrame with engineered income features.
    """

    income_brackets = [
        "$10,000 to $14,999",
        "$15,000 to $24,999", 
        "$25,000 to $34,999",
        "$35,000 to $49,999",
        "$50,000 to $74,999",
        "$75,000 to $99,999",
        "$100,000 to $149,999",
        "$150,000 to $199,999",
        "$200,000 or more"
    ]
    
    # Engineer income features
    data['low_income'] = (data["Less than $10,000"] +
                             data["$10,000 to $14,999"] +
                             data["$15,000 to $24,999"] +
                             data["$25,000 to $34,999"])
    data['middle_income'] = (data["$35,000 to $49,999"] +
                             data["$50,000 to $74,999"] +
                             data["$75,000 to $99,999"])
    data['high_income'] = (data["$100,000 to $149,999"] +
                                    data["$150,000 to $199,999"] +
                                    data["$200,000 or more"])
    data['income_high_to_low_ratio'] = data['high_income'] / (data['low_income']+1)

    income_midpoints = [12.5, 20, 30, 42.5, 62.5, 87.5, 125, 175, 250]

    data['weighted_mean_income'] = sum(
        data[bracket] * midpoint 
        for bracket, midpoint in zip(income_brackets, income_midpoints)
    ) / 100

    # Drop original income columns
    if drop:
        data.drop(columns=["Less than $10,000",
            "$10,000 to $14,999",
            "$15,000 to $24,999",
            "$25,000 to $34,999",
            "$35,000 to $49,999",
            "$50,000 to $74,999",
            "$75,000 to $99,999",
            "$100,000 to $149,999",
            "$150,000 to $199,999",
            "$200,000 or more"], inplace=True)
    
    return data

def engineer_GRAPI(data,drop):

    data['GRAPI_affordable'] = (data['Less than 15.0 percent'] +
                                data['15.0 to 19.9 percent'] + 
                                data['20.0 to 24.9 percent'] + 
                                data['25.0 to 29.9 percent'])

    if drop:
        data.drop(columns=['Less than 15.0 percent',
            '15.0 to 19.9 percent',
            '20.0 to 24.9 percent',
            '25.0 to 29.9 percent',
            '30.0 to 34.9 percent',
            '35.0 percent or more'], inplace=True)
     
    return data 

def engineer_private_insurance(data,drop):

    data['private_insurance_total'] = (data['Employer-based health insurance alone'] + 
                                 data['Direct-purchase health insurance alone'] + 
                                 data['Tricare/military health coverage alone'])
    
    data['economic_stability_ratio'] = data['Employer-based health insurance alone'] / (data['Direct-purchase health insurance alone'] + 1)
    data['economic_vulnerability_ratio'] = data['Employer-based health insurance alone'] / data['private_insurance_total']

    if drop:
        data.drop(columns=['Employer-based health insurance alone',
                           'Direct-purchase health insurance alone',
                           'Tricare/military health coverage alone'], inplace=True)
    
    return data

def engineer_all(data, drop=True):
    """
    Engineer all features in the DataFrame.
    
    Args:
        data (pd.DataFrame): The DataFrame containing the data.
        drop (bool): Whether to drop original columns after engineering.
        
    Returns:
        pd.DataFrame: The DataFrame with all engineered features.
    """
    data = engineer_education(data, drop=drop)
    data = engineer_income(data, drop=drop)
    data = engineer_GRAPI(data, drop=drop)
    data = engineer_private_insurance(data, drop=drop)
    
    return data