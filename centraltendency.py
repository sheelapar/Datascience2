import pandas as pd
from univariant import univariant
import numpy as np

dataset = pd.read_csv('Placement.csv')
# print(dataset.head())

# print(dataset['ssc_p'].mean())
# print(dataset['ssc_p'].median())
# print(dataset['ssc_p'].mode()[0])

# print(dataset.describe())

qual, quant = univariant.qualquan(dataset)
descriptive = pd.DataFrame(columns=quant, index=[
                           'Mean', 'Median', 'Mode', 'q1 :25%', 'q2 :50%', 'q3 :75%', 'q4 :100%'])
for column in quant:
    descriptive.at['Mean', column] = dataset[column].mean()
    descriptive.at['Median', column] = dataset[column].median()
    descriptive.at['Mode', column] = dataset[column].mode()[0]
    descriptive.at['q1 :25%', column] = dataset.describe()[column]['25%']
    descriptive.at['q2 :50%', column] = dataset.describe()[column]['50%']
    descriptive.at['q3 :75%', column] = dataset.describe()[column]['75%']
    descriptive.at['q4 :100%', column] = dataset.describe()[column]['max']

# for column in quant:
#     descriptive.loc['Mean', column] = dataset[column].mean()
#     descriptive.loc['Median', column] = dataset[column].median()
#     descriptive.loc['Mode', column] = dataset[column].mode()[0]
# for column in quant:
#     descriptive.loc['Mean', column] = round(dataset[column].mean(), 2)
#     descriptive.loc['Median', column] = round(dataset[column].median(), 2)
#     descriptive.loc['Mode', column] = round(dataset[column].mode()[0], 2)

# for column in quant:
#     descriptive[column]['Mean'] = round(dataset[column].mean())
#     descriptive[column]['Median'] = round(dataset[column].median())
#     descriptive[column]['Mode'] = round(dataset[column].mode()[0])

print(descriptive)
# print(np.percentile(dataset['ssc_p'], 100))
