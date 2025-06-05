from data_load import load_target, load_features
from data_clean import clean_dataset 
from data_split import split_dataset
from data_train import train_eval_model

if __name__ == "__main__":

    # # Load the target dataset (cancer mortality rates)
    dataset = load_target()
    print('Target dataset loaded')

    # # Load education and income data
    dataset = load_features(dataset)
    print('Features dataset loaded')

    # # clean dataset and prepare for model training 
    dataset_clean = clean_dataset(dataset)
    print('Dataset cleaned')

    # split the dataset for model training
    X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(dataset_clean)
    print('Dataset split into training, validation, and test sets')

    # train and evaluate the model 
    train_eval_model(X_train, X_val, y_train, y_val)
