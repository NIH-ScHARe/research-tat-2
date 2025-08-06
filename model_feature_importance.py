from data_split import split_dataset_cv
from model_pipelines import get_rfr_pipeline

def get_rfr_importance(data):

    # 1. Split the data 
    X_train, X_test, y_train, y_test = split_dataset_cv(data)

    # 2. Define the pipeline 
    rfr_pipeline = get_rfr_pipeline()

    # 3. Fit the pipeline to all the data 
    rfr_pipeline.fit(X_train,y_train)

    # 4. Print features
    selector = rfr_pipeline.named_steps['selectfrommodel']
    selected_features = selector.get_support()
    n_selected = sum(selected_features)
    
    print(f"Original number of features: {X_train.shape[1]}")
    print(f"Selected features: {n_selected}")
    print(f"Feature selection ratio: {n_selected/X_train.shape[1]:.2f}")
    
    # Access feature importances from the final regressor
    final_rf = rfr_pipeline.named_steps['randomforestregressor']
    feature_importances = final_rf.feature_importances_
    
    print(f"\nTop 5 feature importances (after selection):")
    for i, importance in enumerate(sorted(feature_importances, reverse=True)[:5]):
        print(f"Feature {i+1}: {importance:.4f}")
    
    # Print the auto-generated step names for reference
    print(f"\nPipeline steps: {list(rfr_pipeline.named_steps.keys())}")