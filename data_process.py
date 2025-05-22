import pandas as pd

def compute_disparity(baseline,comparison):
    """
    Compute the disparity in cancer rates between two datasets.
    
    Args:
        baseline (pd.DataFrame): DataFrame containing baseline cancer data.
        comparison (pd.DataFrame): DataFrame containing comparison cancer data.

    Returns:
        pd.DataFrame: A DataFrame containing the disparity in cancer rates.    
    """
    # merge the two dataframes on the 'FIPS' column
    merged_df = pd.merge(baseline, comparison, on='County FIPS', suffixes=('_baseline', '_comparison'))

    # calculate the disparity
    merged_df['mortality_rate_disparity'] = merged_df['Age-Adjusted Rate per 100,000_baseline'] - merged_df['Age-Adjusted Rate per 100,000_comparison']

    return merged_df[['County FIPS', 'mortality_rate_disparity']]