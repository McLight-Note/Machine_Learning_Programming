import pandas as pd

df = pd.read_csv('dataset_missing_and_categorical.csv', index_col="Name")
print(df)

ages_over_20 = df[df["Age"] >= 20]
print(ages_over_20)

females = df[df['Gender'] == 'Female']
males = df[df['Gender'] == 'Male']

print('Here are Females\n', females)
print("\n\nHere are Males\n", males)

x = df.iloc[:,:-1]
print(x)

y = df.iloc[:,3]
print(y)