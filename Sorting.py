import pandas as pd

read = pd.read_csv('students.csv')
sorted_data = read.sort_values(by='Score', ascending=False)
read.to_csv('processed_students.csv', index=False)
print(sorted_data.head())

