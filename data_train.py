import numpy as np 
import pandas as pd 
from sklearn.model_selection import cross_validate
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
from data_split import split_dataset_cv
from model_output import save_cv_scores
from model_pipelines import get_rfr_pipeline, get_gbr_pipeline, get_xgbr_pipeline, get_elastic_net_pipeline

# Assume X_train, X_test, y_train, y_test are already defined

def train_XGBR(data, scoring):
    """
    Train an XGBoost Regressor and evaluate its performance on training and test sets.

    Args:
        X_train (pd.DataFrame or np.ndarray): Training feature matrix.
        y_train (pd.Series or np.ndarray): Training target vector.

    Returns:
        model: Trained XGBoost Regressor.
    """
    
    # 1. Split data
    X_train, X_test, y_train, y_test = split_dataset_cv(data)

    # 2. Define pipeline with feature selection 
    pipeline_xgbr = get_xgbr_pipeline()

    # 3. Cross validate model 
    cv_scores = cross_validate(
        pipeline_xgbr, 
        X_train, 
        y_train, 
        cv=5, 
        scoring=scoring,
        return_train_score=True
    )

    # 4. Save cv scores to csv 
    save_cv_scores('xgbr', scoring, cv_scores)

def train_GBR(data, scoring):
    """
    Train a Gradient Boosting Regressor and evaluate its performance on training and test sets.

    Args:
        X_train (pd.DataFrame or np.ndarray): Training feature matrix.
        y_train (pd.Series or np.ndarray): Training target vector.

    Returns:
        model: Trained Gradient Boosting Regressor.
    """
    
    # 1. Split data
    X_train, X_test, y_train, y_test = split_dataset_cv(data)

    # 2. Define pipeline with feature selection
    pipeline_gbr = get_gbr_pipeline()

    # 3. Cross validate model 
    cv_scores = cross_validate(
        pipeline_gbr, 
        X_train, 
        y_train, 
        cv=5, 
        scoring=scoring,
        return_train_score=True
    )

    # 4. Save CV scores to file 
    save_cv_scores('gbr', scoring, cv_scores)

def train_RFR(data, scoring):
    """
    Train a Random Forest Regressor and evaluate its performance on training and test sets.

    Args:
        X_train (pd.DataFrame or np.ndarray): Training feature matrix.
        X_test (pd.DataFrame or np.ndarray): Test feature matrix.
        y_train (pd.Series or np.ndarray): Training target vector.
        y_test (pd.Series or np.ndarray): Test target vector.

    Returns:
        None
    """
    
    # 1. Split data 
    X_train, X_test, y_train, y_test = split_dataset_cv(data)

    # 2. Define pipeline with feature selection 
    rfr_pipeline = get_rfr_pipeline()

    # 3. Cross validate model 
    cv_scores = cross_validate(
        rfr_pipeline, 
        X_train, 
        y_train, 
        cv=5, 
        scoring=scoring,
        return_train_score=True
    )

    # 4. Save CV scores to file
    save_cv_scores('random_forest', scoring, cv_scores)

def train_elastic_net(data, scoring):
    """
    Train a Linear Regression model and return the trained model.

    Args:
        X_train (pd.DataFrame or np.ndarray): Training feature matrix.
        y_train (pd.Series or np.ndarray): Training target vector.

    Returns:
        model: Trained Elastic Net.
    """
    
    # 1. Split the Data 
    X_train, X_test, y_train, y_test = split_dataset_cv(data)

    # 2. Define pipeline with scaling 
    pipeline_en = get_elastic_net_pipeline()

    # 3. Cross validate model 
    cv_scores = cross_validate(
        pipeline_en, 
        X_train, 
        y_train, 
        cv=5, 
        scoring=scoring,
        return_train_score=True
    )

    # 4. Save cv scores to csv 
    save_cv_scores('elastic_net', scoring, cv_scores)

def evaluate_model(rf, X_train, X_test, y_train, y_test):

    # 2. Predict on training and test sets
    y_train_pred = rf.predict(X_train)
    y_test_pred = rf.predict(X_test)

    # 3. Calculate metrics 
    metrics_data = []
    
    # RMSE
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    val_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
    metrics_data.append(['RMSE', train_rmse, val_rmse, val_rmse - train_rmse])

    # MAE
    train_mae = mean_absolute_error(y_train, y_train_pred)
    val_mae = mean_absolute_error(y_test, y_test_pred)
    metrics_data.append(['MAE', train_mae, val_mae, val_mae - train_mae])
    
    # R²
    train_r2 = r2_score(y_train, y_train_pred)
    val_r2 = r2_score(y_test, y_test_pred)
    metrics_data.append(['R²', train_r2, val_r2, train_r2 - val_r2])
    
    # Create DataFrame for better visualization
    df = pd.DataFrame(metrics_data, columns=['Metric', 'Training', 'Validation', 'Gap'])
    df['Gap_Percentage'] = np.where(df['Metric'] == 'R²', 
                                   (df['Gap'] / df['Training']) * 100,
                                   (df['Gap'] / df['Training']) * 100)
    
    print("=== Comprehensive Train-Val Comparison ===")
    print(df.round(4))

    return df


def train_eval_model(X_train, X_test, y_train, y_test):
    """
    Train a Random Forest Regressor and evaluate its performance on training and test sets.

    Args:
        X_train (pd.DataFrame or np.ndarray): Training feature matrix.
        X_test (pd.DataFrame or np.ndarray): Test feature matrix.
        y_train (pd.Series or np.ndarray): Training target vector.
        y_test (pd.Series or np.ndarray): Test target vector.

    Returns:
        None
    """
    rf = train_RFR(X_train, y_train)
    evaluate_model(rf, X_train, X_test, y_train, y_test)



def comprehensive_train_val_comparison(model, X_train, y_train, X_val, y_val):
    """
    Comprehensive comparison of training vs validation metrics
    """
    # Get predictions
    y_train_pred = model.predict(X_train)
    y_val_pred = model.predict(X_val)
    
    # Calculate all metrics
    metrics_data = []
    
    # RMSE
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    val_rmse = np.sqrt(mean_squared_error(y_val, y_val_pred))
    metrics_data.append(['RMSE', train_rmse, val_rmse, val_rmse - train_rmse])
    
    # MAE
    train_mae = mean_absolute_error(y_train, y_train_pred)
    val_mae = mean_absolute_error(y_val, y_val_pred)
    metrics_data.append(['MAE', train_mae, val_mae, val_mae - train_mae])
    
    # R²
    train_r2 = r2_score(y_train, y_train_pred)
    val_r2 = r2_score(y_val, y_val_pred)
    metrics_data.append(['R²', train_r2, val_r2, train_r2 - val_r2])
    
    # Create DataFrame for better visualization
    df = pd.DataFrame(metrics_data, columns=['Metric', 'Training', 'Validation', 'Gap'])
    df['Gap_Percentage'] = np.where(df['Metric'] == 'R²', 
                                   (df['Gap'] / df['Training']) * 100,
                                   (df['Gap'] / df['Training']) * 100)
    
    print("=== Comprehensive Train-Val Comparison ===")
    print(df.round(4))
    
    # Visual comparison
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    metrics_names = ['RMSE', 'MAE', 'R²']
    train_vals = [train_rmse, train_mae, train_r2]
    val_vals = [val_rmse, val_mae, val_r2]
    
    for i, (metric, train_val, val_val) in enumerate(zip(metrics_names, train_vals, val_vals)):
        x = ['Training', 'Validation']
        y = [train_val, val_val]
        
        axes[i].bar(x, y, color=['blue', 'red'], alpha=0.7)
        axes[i].set_title(f'{metric}')
        axes[i].set_ylabel(metric)
        
        # Add gap annotation
        gap = val_val - train_val if metric != 'R²' else train_val - val_val
        axes[i].annotate(f'Gap: {gap:.4f}', 
                        xy=(0.5, max(y) * 0.9), 
                        ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
    return df

def comprehensive_train_eval_model(X_train, X_test, y_train, y_test):
    """ Comprehensive evaluation of a Random Forest Regressor on training and test sets.
    
    Args:
        X_train (pd.DataFrame or np.ndarray): Training feature matrix.
        X_test (pd.DataFrame or np.ndarray): Test feature matrix.
        y_train (pd.Series or np.ndarray): Training target vector.
        y_test (pd.Series or np.ndarray): Test target vector.

    Returns:
        None
    """
    
    rf = train_RFR(X_train, y_train)
    comprehensive_train_val_comparison(rf, X_train, X_test, y_train, y_test)


