import pandas as pd 
from data_load import load_mortality_data, load_features
import statsmodels.formula.api as smf 
from data_clean import drop_incomplete_msas 

# data = load_mortality_data()

# data = load_features(data)

# data = data.rename(columns={
#         'Less than 9th grade': 'less_than_9th_grade',
#         '9th to 12th grade, no diploma': 'ninth_to_12th_no_diploma',
#         'High school graduate (includes equivalency)': 'high_school_graduate',
#         'Some college, no degree': 'some_college',
#         'Associate\'s degree': 'associates_degree',
#         'Bachelor\'s degree': 'bachelors_degree',
#         'Graduate or professional degree': 'graduate_or_professional_degree',
#     })

# data = drop_incomplete_msas(data, msa_col="msa_code", year_col="year")


# data.to_csv('data/MSA_mortality_with_features.csv', index=False)

data = pd.read_csv('data/MSA_mortality_with_features.csv')

model = smf.mixedlm(
    "mortality_rate ~ year + less_than_9th_grade + ninth_to_12th_no_diploma", 
    data=data,
    groups=data["msa_code"],
    re_formula="~year"
)

result = model.fit()
print(result.summary())