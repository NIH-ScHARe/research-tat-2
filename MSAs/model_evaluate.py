import numpy as np

def mixedlm_r2(result, df, response_col):
    """
    Compute marginal and conditional R² for a fitted statsmodels MixedLM.
    
    result: fitted MixedLMResults object
    df: original dataframe used to fit
    response_col: name of response variable
    """
    # Response variance
    var_y = np.var(df[response_col], ddof=1)

    # Fixed effects predictions
    y_fixed = result.fittedvalues
    var_fixed = np.var(y_fixed, ddof=1)

    # Random effect variance (sum of estimated group variances)
    var_random = sum([v for v in result.cov_re.values.flatten()])

    # Residual variance
    var_resid = result.scale

    # Marginal R² (fixed effects only)
    r2_marginal = var_fixed / (var_fixed + var_random + var_resid)

    # Conditional R² (fixed + random)
    r2_conditional = (var_fixed + var_random) / (var_fixed + var_random + var_resid)

    return r2_marginal, r2_conditional
