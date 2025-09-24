import pandas as pd 
import statsmodels.formula.api as smf 

def fit_model():

    data = pd.read_csv('MSAs/data/data_02_engineered.csv')

    formula = (
        "mortality_rate ~ year_centered + hs + college_plus + middle_income + high_income + english_only"
    )

    cols = ["mortality_rate", "year_centered", "hs", "college_plus",
            "middle_income", "high_income", "english_only", "msa_code"]

    data = data[cols]

    model = smf.mixedlm(
        formula, 
        data=data,
        groups=data["msa_code"],
        # re_formula="~year_centered"
    )

    result = model.fit()

    return result, data