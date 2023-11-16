import pandas
import imodels
import numpy as np
from datasets import load_dataset

dataset = load_dataset("imodels/credit-card")
df = pandas.DataFrame(dataset['train'])
X = df.drop(columns=['default.payment.next.month'])
y = df['default.payment.next.month'].values

## duplicates
df_without_duplicates = pandas.DataFrame(dataset['train'])
df_without_duplicates.drop_duplicates(inplace=True)

# print("With duplicates:")
# print(df)
#
# print("Without duplicates:")
# print(df_without_duplicates)

##corelation

#print("Correlation between age and bal limit is: ", df['limit_bal'].corr(df['age']))

##adding new column
#df['sum_of_bill_amt'] = df['bill_amt1'] + df['bill_amt2'] + df['bill_amt3'] + df['bill_amt4'] + df['bill_amt5'] + df['bill_amt6']
#print(df['sum_of_bill_amt'])

##sort by age
df_sort_by_age = df.sort_values(by='age', ascending=False)
print(df_sort_by_age['age'].head(10))

