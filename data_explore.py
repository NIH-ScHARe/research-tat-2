import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns

def plot_distribution(data, column_name):

    # drop rows with null values in the specified column
    dropped_data = data[column_name].dropna()

    # plot mortality data 
    plt.figure(figsize=(4,3))
    counts, _, _ = plt.hist(dropped_data, bins=30, color='black', alpha=0.7, density=True)
    plt.boxplot(
        dropped_data,
        vert=False,
        positions=[counts.max() * 1.1],
        widths=counts.max() * 0.05,
        patch_artist=True,
        boxprops=dict(facecolor='black', color='black'),
        medianprops=dict(color='white'),
        whiskerprops=dict(color='black'),
        capprops=dict(color='black'),
        flierprops=dict(marker='.', markerfacecolor='black', markeredgecolor='none', markersize=5)
    )
    plt.ylim([0,counts.max() * 1.2])
    plt.yticks([])
    plt.xlabel(column_name)
    plt.tight_layout()  
    plt.show()


def explore_raw_data():
    """
    Load and explore the raw dataset.
    """
    # Load the raw dataset
    raw_data = pd.read_csv('dataset_raw.csv')

    # for col in raw_data.columns:
    #     plot_distribution(raw_data, col)

    plot_distribution(raw_data,'dual_enrollee_percent') 

def explore_cleaned_data():

    cleaned_data = pd.read_csv('dataset_cleaned.csv')

    
    # get the rows of null values in the 'doctor_visit_rate' column
    null_rows = cleaned_data[cleaned_data['doctor_visit_rate'].isnull()]
    
    data2 = cleaned_data.copy()

    # impute values in 'doctor_visit_rate' with the median of the column
    data2['doctor_visit_rate'].fillna(data2['doctor_visit_rate'].median(), inplace=True)

    data2.describe()

def feature_correlation(features):

    plt.figure(figsize=(7, 6))
    correlation_matrix = features.corr()
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    sns.heatmap(
        correlation_matrix,
        mask=mask,
        annot=True,           # Show correlation values
        cmap='coolwarm',
        center=0,
        fmt='.2f',            # Format to 2 decimal places
        square=True
    )
    plt.title('Feature Correlation Matrix')
    plt.tight_layout()
    plt.show()