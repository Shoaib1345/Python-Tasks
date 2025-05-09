#Display the column names, data types, and basic statistics of the dataset
import pandas as pd
read=pd.read_csv('students.csv')
print(read.dtypes)
read.to_csv('processed_students.csv', index=False)