from data_load import load_target, load_features
from data_clean import clean_dataset 

if __name__ == "__main__":

    # Load the target dataset (cancer mortality rates)
    dataset = load_target()

    # Load education and income data
    dataset = load_features(dataset)

    # clean dataset and prepare for model training 
    dataset_clean = clean_dataset(dataset)



    # print(dataset.columns)

    # education_data = get_education_data('2022', 'county', as_percent=True)
    # income_data = get_household_income_data('2022', 'county', as_percent=True)


    

