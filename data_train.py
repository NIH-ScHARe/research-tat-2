from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Assume X_train, X_test, y_train, y_test are already defined

def train_RFR(X_train, y_train):
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
    
    # 1. Train the Random Forest Regressor
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    return rf

def evaluate_model(rf, X_train, X_test, y_train, y_test):

    # 2. Predict on training and test sets
    y_train_pred = rf.predict(X_train)
    y_test_pred = rf.predict(X_test)

    # 3. Calculate mean squared error for both sets
    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)

    print(f"Train MSE: {train_mse:.3f}")
    print(f"Test MSE: {test_mse:.3f}")

    # 4. Interpret the results
    if train_mse > 1.5 * test_mse:
        print("Possible underfitting (high bias).")
    elif test_mse > 1.5 * train_mse:
        print("Possible overfitting (high variance).")
    else:
        print("Model is reasonably balanced between bias and variance.")

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

