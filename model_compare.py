import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


elastic_net = pd.read_csv('model evaluation/metrics_elastic_net.csv')
rfr = pd.read_csv('model evaluation/metrics_random_forest.csv')
gbr = pd.read_csv('model evaluation/metrics_gbr.csv')
xgbr = pd.read_csv('model evaluation/metrics_xgbr.csv')

plt.figure(figsize=(16,3))
plt.subplot(1,3,1)
plt.title('MAE')
plt.bar(1,-elastic_net['train_mean'][0], label='Training', color='blue',yerr=elastic_net['train_std'][0])
plt.bar(2,-elastic_net['test_mean'][0], label='Validation', color='red',yerr=elastic_net['test_std'][0])
plt.bar(4,-rfr['train_mean'][0], color='blue',yerr=rfr['train_std'][0])
plt.bar(5,-rfr['test_mean'][0], color='red',yerr=rfr['test_std'][0])
plt.bar(7,-gbr['train_mean'][0], color='blue',yerr=gbr['train_std'][0])
plt.bar(8,-gbr['test_mean'][0], color='red',yerr=gbr['test_std'][0])
plt.bar(10,-xgbr['train_mean'][0], color='blue',yerr=xgbr['train_std'][0])
plt.bar(11,-xgbr['test_mean'][0], color='red',yerr=xgbr['test_std'][0]) 
plt.xticks([1.5, 4.5, 7.5, 10.5], 
           ['Elastic Net', 'Random Forest', 'Gradient Boosting', 'XGBoost'])
plt.legend(frameon=0)
plt.ylim(0,170)

plt.subplot(1,3,2)
plt.title('RMSE')
plt.bar(1,-elastic_net['train_mean'][1], label='Training', color='blue',yerr=elastic_net['train_std'][1])
plt.bar(2,-elastic_net['test_mean'][1], label='Validation', color='red',yerr=elastic_net['test_std'][1])
plt.bar(4,-rfr['train_mean'][1], label='Training', color='blue',yerr=rfr['train_std'][1])
plt.bar(5,-rfr['test_mean'][1], label='Validation', color='red',yerr=rfr['test_std'][1])
plt.bar(7,-gbr['train_mean'][1], label='Training', color='blue',yerr=gbr['train_std'][1])
plt.bar(8,-gbr['test_mean'][1], label='Validation', color='red',yerr=gbr['test_std'][1])
plt.bar(10,-xgbr['train_mean'][1], label='Training', color='blue',yerr=xgbr['train_std'][1])
plt.bar(11,-xgbr['test_mean'][1], label='Validation', color='red',yerr=xgbr['test_std'][1]) 
plt.xticks([1.5, 4.5, 7.5, 10.5], 
           ['Elastic Net', 'Random Forest', 'Gradient Boosting', 'XGBoost'])
plt.ylim(0,170)

plt.subplot(1,3,3)
plt.title('$R^2$')
plt.bar(1,elastic_net['train_mean'][2], label='Training', color='blue',yerr=elastic_net['train_std'][2])
plt.bar(2,elastic_net['test_mean'][2], label='Validation', color='red',yerr=elastic_net['test_std'][2])
plt.bar(4,rfr['train_mean'][2], label='Training', color='blue',yerr=rfr['train_std'][2])
plt.bar(5,rfr['test_mean'][2], label='Validation', color='red',yerr=rfr['test_std'][2])
plt.bar(7,gbr['train_mean'][2], label='Training', color='blue',yerr=gbr['train_std'][2])
plt.bar(8,gbr['test_mean'][2], label='Validation', color='red',yerr=gbr['test_std'][2])
plt.bar(10,xgbr['train_mean'][2], label='Training', color='blue',yerr=xgbr['train_std'][2])
plt.bar(11,xgbr['test_mean'][2], label='Validation', color='red',yerr=xgbr['test_std'][2]) 
plt.xticks([1.5, 4.5, 7.5, 10.5], 
           ['Elastic Net', 'Random Forest', 'Gradient Boosting', 'XGBoost'])
plt.ylim(0,1)

plt.tight_layout()
plt.show()


