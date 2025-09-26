import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor

data = pd.read_csv('MSAs/data/data_02_engineered.csv')

X = data[["less_than_hs", "college_plus", "year_centered"]].copy()

vif = pd.DataFrame({
    "feature": X.columns,
    "VIF": [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
})
print(vif.sort_values("VIF", ascending=False))

# formula = (
#     "mortality_rate ~ year_centered + hs + college_plus"
# )

# cols = ["mortality_rate", "year_centered", "hs", "college_plus",
#         "middle_income", "high_income", "english_only", 
#         "employer_based_health_insurance", "direct_purchase_health_insurance",
#             "tricare_health_insurance", "medicare", "medicaid", "VA", "msa_code"]

# data = data[cols]

# model = smf.mixedlm(
#     formula, 
#     data=data,
#     groups=data["msa_code"],
#     # re_formula="~year_centered"
# )

# result = model.fit()