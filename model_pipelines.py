from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import ElasticNet
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor

def get_elastic_net_pipeline():

    pipeline_en = make_pipeline(
        RobustScaler(),
        ElasticNet(
            alpha=1.0, 
            l1_ratio=0.5, 
            random_state=42)
    )

    return pipeline_en

def get_rfr_pipeline():

    rfr_pipeline = make_pipeline(
        SelectFromModel(
            RandomForestRegressor(
                n_estimators=100,
                random_state=42,
            ),
            threshold='median'  # Select features with importance above median
        ),
        RandomForestRegressor(
            n_estimators=100,           # Fewer trees
            max_depth=10,              # Limit tree depth
            min_samples_split=20,      # Require more samples to split
            min_samples_leaf=10,       # Require more samples in leaf nodes
            max_features='sqrt',       # Limit features per split
            random_state=42
        )
    )

    return rfr_pipeline

def get_gbr_pipeline():

    pipeline_gbr = make_pipeline(
        SelectFromModel(
            GradientBoostingRegressor(
                n_estimators=50, 
                random_state=42), 
            threshold='median'),
        GradientBoostingRegressor(
            loss='huber',
            alpha=0.9,               # Use Huber loss with alpha=0.9
            n_estimators=50,         # Reduce from 100+ to 50
            learning_rate=0.05,      # Reduce from 0.1 to 0.05 
            max_depth=3,             # Reduce from 6+ to 3-4
            min_samples_split=20,    # Increase from 2 to 20
            min_samples_leaf=10,     # Increase from 1 to 10
            subsample=0.8,           # Use only 80% of samples per tree
            max_features='sqrt',     # Use only sqrt(n_features) per split
            random_state=42
        )
    )

    return pipeline_gbr

def get_xgbr_pipeline():

    pipeline_xgbr = make_pipeline(
        SelectFromModel(
            XGBRegressor(
                n_estimators=100, 
                learning_rate=0.1, 
                max_depth=6), 
            threshold='median'),
        XGBRegressor(
            objective='reg:tweedie', # more robust to outliers than square error 
            n_estimators=50,         # Reduce from 100+ to 50
            learning_rate=0.05,      # Reduce from 0.1 to 0.05 
            max_depth=3,             # Reduce from 6+ to 3-4
            min_child_weight=10,     # Increase from 1 to 10
            subsample=0.8,           # Use only 80% of samples per tree
            colsample_bytree=0.8,    # Use only 80% of features per split
            random_state=42
        )
    )

    return pipeline_xgbr