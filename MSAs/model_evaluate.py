import numpy as np
import pandas as pd 
from statsmodels.stats.outliers_influence import variance_inflation_factor

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

def get_vifs(res):

    # 1) Get fixed-effects design matrix and names
    X = pd.DataFrame(res.model.exog, columns=res.model.exog_names)

    # 2) Drop the intercept column for VIF (it will otherwise explode)
    X_no_intercept = X.loc[:, [c for c in X.columns
                            if c.lower() != "intercept" and not c.lower().startswith("intercept")]]

    # 3) Optional sanity checks
    rank = np.linalg.matrix_rank(X_no_intercept.values)
    print(f"Columns: {X_no_intercept.shape[1]}, Matrix rank: {rank}")  # rank < ncols ⇒ exact collinearity
    cond_num = np.linalg.cond(X_no_intercept.values)
    print(f"Condition number: {cond_num:,.1f}")                        # >30 concerning, >100 severe

    # 4) Compute VIFs
    vif = pd.DataFrame({
        "feature": X_no_intercept.columns,
        "VIF": [variance_inflation_factor(X_no_intercept.values, i)
                for i in range(X_no_intercept.shape[1])]
    }).sort_values("VIF", ascending=False).reset_index(drop=True)

    print(vif)
