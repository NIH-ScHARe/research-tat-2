import pandas as pd 
from data_clean import clean_dataset 
from data_split import split_dataset
from data_train import train_elastic_net, train_RFR, train_GBR, train_XGBR, evaluate_model
from data_engineer import engineer_all
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.feature_selection import SelectKBest, f_regression, SelectFromModel

from data_explore import feature_correlation

raw_data = pd.read_csv('dataset_raw.csv')

id = 'FIPS'
target = 'mortality_rate'
features = ['Less than 9th grade',
            '9th to 12th grade, no diploma',
            'High school graduate (includes equivalency)',
            'Some college, no degree',
            'Associate\'s degree',
            'Bachelor\'s degree',
            'Graduate or professional degree',
            "Less than $10,000",
            "$10,000 to $14,999",
            "$15,000 to $24,999",
            "$25,000 to $34,999",
            "$35,000 to $49,999",
            "$50,000 to $74,999",
            "$75,000 to $99,999",
            "$100,000 to $149,999",
            "$150,000 to $199,999",
            "$200,000 or more",
            'Less than 15.0 percent',
            '15.0 to 19.9 percent',
            '20.0 to 24.9 percent',
            '25.0 to 29.9 percent',
            '30.0 to 34.9 percent',
            '35.0 percent or more',
            'English only',
            'Spanish',
            'Other Indo-European languages',
            'Asian and Pacific Islander languages',
            'Other languages',
            'With a computer',
            'With a broadband Internet subscription',
            'doctor_visit_rate', 
            'self_care_disability_rate', 
            'frequent_mental_distress_rate', 
            'health_insurance_access_rate',
            'independent_living_disability_rate',
            'food_insecurity_rate',
            'housing_insecurity_rate',
            'social_isolation_rate',
            'lack_reliable_transportation_rate',
            'lack_emotional_support_rate',
            'total_medicare_percent',
            'Employer-based health insurance alone or in combination',
            'Direct-purchase health insurance alone or in combination',
            'Tricare/military health insurance alone or in combination',
            'Medicare coverage alone or in combination',
            'Medicaid/means-tested public coverage alone or in combination',
            'VA health care coverage alone or in combination',
            'Male',
            'Female',
            'White',
            'Black or African American',
            'American Indian and Alaska Native',
            'Asian',
            'Native Hawaiian and Other Pacific Islander',
            'Some Other Race']
subset = raw_data[[id, target] + features].copy()

# drop rows with missing target values 
subset.dropna(subset='mortality_rate',inplace=True)

# examine correlation of features 
# feature_correlation(subset[features])

# fill missing data with median imputation 
for feature in features:
    # print(f"Number of null columns for column {feature}: {subset[feature].isnull().sum()}")
    subset.fillna({feature: subset[feature].median()}, inplace=True)

# examine correaltion after imputation
# feature_correlation(subset[features])

# create copy of data for each model 
subset_rfr = subset.copy()
subset_en = subset.copy()
subset_gbr = subset.copy()
subset_xgbr = subset.copy()

# address outliers 

# FEATURE ENGINEERING 
subset_en = engineer_all(subset_en, drop=True)
subset_rfr = engineer_all(subset_rfr, drop=False)
subset_gbr = engineer_all(subset_gbr, drop=False)
subset_xgbr = engineer_all(subset_xgbr, drop=False)

# Elastic Net Regression
# split data 
X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(subset_en)

# scale data 
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

# train and evaluate model 
elastic_net = train_elastic_net(X_train_scaled, y_train)
print('Elastic Net Regressor')
metrics_elastic_net = evaluate_model(elastic_net, X_train_scaled, X_val_scaled, y_train, y_val)
print('\n')

# Random Forest Regressor 
# split data 
X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(subset_rfr)

# Feature Selection 
rf_selector = RandomForestRegressor(n_estimators=100, random_state=42)
feature_selector = SelectFromModel(rf_selector, threshold='median')
X_train_selected = feature_selector.fit_transform(X_train, y_train)
X_test_selected = feature_selector.transform(X_val)

# train and evaluate model 
RFR = train_RFR(X_train_selected, y_train)
print('Random Forest Regressor')
metrics_RFR = evaluate_model(RFR, X_train_selected, X_test_selected, y_train, y_val)
print('\n')


# Gradient Boosting Regressor
# split data
X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(subset_gbr)

# feature selection
gbr_selector = GradientBoostingRegressor(n_estimators=50, random_state=42)
selector = SelectFromModel(gbr_selector, threshold='median')
X_train_sel = selector.fit_transform(X_train, y_train)
X_val_sel = selector.transform(X_val)

# train and evaluate model 
GBR = train_GBR(X_train_sel, y_train)
print('Gradient Boosting Regressor')
metrics_GBR = evaluate_model(GBR, X_train_sel, X_val_sel, y_train, y_val)
print('\n')

# XGBoost Regressor
# split data
X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(subset_xgbr)

# feature selection
xgbr_selector = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=6)
selector = SelectFromModel(xgbr_selector, threshold='median')
X_train_sel = selector.fit_transform(X_train, y_train)
X_val_sel = selector.transform(X_val)

# train and evaluate model 
XGBR = train_XGBR(X_train_sel, y_train)
print('XGBoost Regressor')
metrics_XGBR = evaluate_model(XGBR, X_train_sel, X_val_sel, y_train, y_val)
print('\n')

# save metrics to CSV file 
metrics_elastic_net.to_csv('model evaluation/metrics_elastic_net.csv', index=False)
metrics_RFR.to_csv('model evaluation/metrics_RFR.csv', index=False)
metrics_GBR.to_csv('model evaluation/metrics_GBR.csv', index=False)
metrics_XGBR.to_csv('model evaluation/metrics_XGBR.csv', index=False)
