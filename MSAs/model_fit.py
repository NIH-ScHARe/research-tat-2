import pandas as pd 
import statsmodels.formula.api as smf 

def fit_model():

    data = pd.read_csv('MSAs/data/data_02_engineered.csv')

    model = smf.mixedlm(
        "mortality_rate ~ year_centered + less_than_hs + hs + college_plus + low_income + middle_income + high_income", 
        data=data,
        groups=data["msa_code"],
        re_formula="~year"
    )

    result = model.fit()

    return result, data