import pandas as pd 
from data_clean import drop_incomplete_msas 
from skbio.stats.composition import ilr, closure
import statsmodels.formula.api as smf
from model_evaluate import mixedlm_r2

raw_data = pd.read_csv('MSAs/data/data_00_raw.csv')
data = drop_incomplete_msas(raw_data, msa_col="msa_code", year_col="year")

# rename education columns 
data = data.rename(columns={
    "Less than 9th grade" : "lt9",
    "9th to 12th grade, no diploma": "ninth12",
    "High school graduate (includes equivalency)": "hs",
    "Some college, no degree": "somecol",
    "Associate's degree": "assoc",
    "Bachelor's degree": "ba",
    "Graduate or professional degree": "grad"
})

# center years for interpretable intercepts 
data["year_centered"] = data["year"] - 2018

# Select the compositional columns
edu_cols = ["lt9","ninth12","hs","somecol","assoc","ba","grad"]

# Ensure closure (rescale so each row sums to 1)
edu = closure(data[edu_cols])

# Apply ILR transform
edu_ilr = ilr(edu)

# Convert to DataFrame
ilr_df = pd.DataFrame(edu_ilr, 
                      columns=[f"ilr_{i+1}" for i in range(edu_ilr.shape[1])],
                      index=data.index)

# Add back to your data
df = pd.concat([data, ilr_df], axis=1)

# Example: outcome y, grouping variable msa
md = smf.mixedlm("mortality_rate ~ ilr_1 + ilr_2 + ilr_3 + ilr_4 + ilr_5 + ilr_6 + year_centered",
                 data=df, groups=df["msa_code"])
res = md.fit(method="lbfgs")
print(res.summary())
r2_m, r2_c = mixedlm_r2(res, df, "mortality_rate")
print(f"Marginal R²: {r2_m:.3f}, Conditional R²: {r2_c:.3f}")

