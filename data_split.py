from sklearn.model_selection import train_test_split

def split_for_random_forest(X, y, test_size=0.2, val_size=0.1, random_state=42):
    """
    Splits features and target into training, validation, and test sets for a Random Forest Regressor.

    Args:
        X (pd.DataFrame or np.ndarray): Feature matrix.
        y (pd.Series or np.ndarray): Target vector.
        test_size (float): Proportion of the dataset to include in the test split.
        val_size (float): Proportion of the dataset to include in the validation split.
        random_state (int): Random seed for reproducibility.

    Returns:
        X_train, X_val, X_test, y_train, y_val, y_test: Split datasets.
    """
    # First split into train+val and test
    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    # Then split train+val into train and val
    val_relative_size = val_size / (1 - test_size)
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=val_relative_size, random_state=random_state
    )
    return X_train, X_val, X_test, y_train, y_val, y_test

def split_dataset(dataset, target_column='mortality_rate', test_size=0.2, val_size = 0.1, random_state=42):
    """
    Splits the dataset into training and test sets.

    Args:
        dataset (pd.DataFrame): The dataset to split.
        target_column (str): The name of the target column.
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Random seed for reproducibility.

    Returns:
        X_train, X_test, y_train, y_test: Split datasets.
    """
    # Separate features and target
    X = dataset.drop(columns=['FIPS',target_column])
    y = dataset[target_column]
    
    return split_for_random_forest(X, y, test_size, val_size, random_state)