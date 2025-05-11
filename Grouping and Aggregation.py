import pandas as pd
read = pd.read_csv('students.csv')
subject_avg = read.groupby('Subject')['Score'].mean()
print(subject_avg)
read.to_csv('processed_students.csv', index=False)