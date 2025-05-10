import pandas as pd
read = pd.read_csv('students.csv')
null=read['Score'].isnull().sum()
mean_values=read['Grade'].mean()
read['Score']=read['Score'].fillna(mean_values)
print(read['Score'])
read.to_csv('processed_students.csv', index=False)
