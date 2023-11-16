import pandas
from datasets import load_dataset
import matplotlib.pyplot as plt

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

print("Correlation between age and bal limit is: ", df['limit_bal'].corr(df['age']))

##adding new column
df['sum_of_bill_amt'] = df['bill_amt1'] + df['bill_amt2'] + df['bill_amt3'] + df['bill_amt4'] + df['bill_amt5'] + df['bill_amt6']
#print(df['sum_of_bill_amt'])

##sort by age
df_sort_by_age = df.sort_values(by='age', ascending=False)

education_columns = df_sort_by_age[['education:1', 'education:2', 'education:3', 'education:4', 'education:5', 'education:6']].head(10)
education_dictionary = {1: "graduate school", 2: "university", 3: "high school", 4: "others", 5: "unknown", 6: "unknown"}
for i, column in enumerate(education_columns, 1):
    if (df_sort_by_age[column] == 1.0).any():
        df_sort_by_age.loc[df_sort_by_age[column] == 1.0, 'education'] = education_dictionary[i]

print((df_sort_by_age[['limit_bal', 'age', 'education', 'sum_of_bill_amt']].head(10)).to_markdown(index=False))


#histogram
fig, axs = plt.subplots(3, 1, figsize=(10,15))
axs[0].hist(df['limit_bal'], bins=120)
axs[0].set_title('histogram limitu kredytu')

axs[1].hist(df['age'], bins=60)
axs[1].set_title('histogram wieku')

axs[2].scatter( df['age'], df['limit_bal'],)
axs[2].set_title('Zależność limitu kredytu od wieku')
axs[2].set_xlabel('Wiek')
axs[2].set_ylabel('Limit kredytu')

plt.show()