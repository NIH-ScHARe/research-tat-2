import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


elastic_net = pd.read_csv('model evaluation/metrics_elastic_net.csv')
rfr = pd.read_csv('model evaluation/metrics_RFR.csv')
gbr = pd.read_csv('model evaluation/metrics_GBR.csv')
xgbr = pd.read_csv('model evaluation/metrics_XGBR.csv')

plt.figure(figsize=(16,3))
plt.subplot(1,3,1)
plt.title('RMSE')
plt.bar(1,elastic_net['Training'][0], label='Training', color='blue')
plt.bar(2,elastic_net['Validation'][0], label='Validation', color='red')
plt.bar(4,rfr['Training'][0], color='blue')
plt.bar(5,rfr['Validation'][0], color='red')
plt.bar(7,gbr['Training'][0], color='blue')
plt.bar(8,gbr['Validation'][0], color='red')
plt.bar(10,xgbr['Training'][0], color='blue')
plt.bar(11,xgbr['Validation'][0], color='red') 
plt.xticks([1.5, 4.5, 7.5, 10.5], 
           ['Elastic Net', 'Random Forest', 'Gradient Boosting', 'XGBoost'])
plt.legend(frameon=0)
plt.ylim(0,170)

plt.subplot(1,3,2)
plt.title('MAE')
plt.bar(1,elastic_net['Training'][1], label='Training', color='blue')
plt.bar(2,elastic_net['Validation'][1], label='Validation', color='red')
plt.bar(4,rfr['Training'][1], label='Training', color='blue')
plt.bar(5,rfr['Validation'][1], label='Validation', color='red')
plt.bar(7,gbr['Training'][1], label='Training', color='blue')
plt.bar(8,gbr['Validation'][1], label='Validation', color='red')
plt.bar(10,xgbr['Training'][1], label='Training', color='blue')
plt.bar(11,xgbr['Validation'][1], label='Validation', color='red') 
plt.xticks([1.5, 4.5, 7.5, 10.5], 
           ['Elastic Net', 'Random Forest', 'Gradient Boosting', 'XGBoost'])
plt.ylim(0,170)

plt.subplot(1,3,3)
plt.title('$R^2$')
plt.bar(1,elastic_net['Training'][2], label='Training', color='blue')
plt.bar(2,elastic_net['Validation'][2], label='Validation', color='red')
plt.bar(4,rfr['Training'][2], label='Training', color='blue')
plt.bar(5,rfr['Validation'][2], label='Validation', color='red')
plt.bar(7,gbr['Training'][2], label='Training', color='blue')
plt.bar(8,gbr['Validation'][2], label='Validation', color='red')
plt.bar(10,xgbr['Training'][2], label='Training', color='blue')
plt.bar(11,xgbr['Validation'][2], label='Validation', color='red') 
plt.xticks([1.5, 4.5, 7.5, 10.5], 
           ['Elastic Net', 'Random Forest', 'Gradient Boosting', 'XGBoost'])
plt.ylim(0,1)

plt.tight_layout()
plt.show()


