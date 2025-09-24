from data_load import load_data
from data_clean import clean_data
from data_engineer import engineer_data 
from model_fit import fit_model 
from model_evaluate import mixedlm_r2 

# load raw data and save 
# load_data()

# clean data 
# clean_data()

# engineer data 
# engineer_data()

# fit and evaluate model 
result, data = fit_model()
print(result.summary())
r2_m, r2_c = mixedlm_r2(result, data, "mortality_rate")
print(f"Marginal R²: {r2_m:.3f}, Conditional R²: {r2_c:.3f}")
