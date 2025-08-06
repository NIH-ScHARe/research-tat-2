import pandas as pd 

def save_cv_scores(model,scoring,cv_scores):
    print(f"=== {model} Cross-Validation Scores ===")
    results = []
    for metric in scoring:
        test_scores = cv_scores[f'test_{metric}']
        train_scores = cv_scores[f'train_{metric}']
        test_mean = test_scores.mean()
        test_std = test_scores.std()
        train_mean = train_scores.mean()
        train_std = train_scores.std()
        print(f"{metric.capitalize()} - Test: {test_mean:.4f} (+/- {test_std * 2:.4f})")
        print(f"{metric.capitalize()} - Train: {train_mean:.4f} (+/- {train_std * 2:.4f})")
        results.append({
            'metric': metric,
            'test_mean': test_mean,
            'test_std': test_std,
            'train_mean': train_mean,
            'train_std': train_std
        })

    # Save results to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv(f"model evaluation/metrics_{model}.csv", index=False)