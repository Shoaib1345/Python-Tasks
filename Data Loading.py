#Load a CSV file named 'students.csv' containing student records.Display the first 5 rows.Ensure the file has
#at least 5 columns(e.g., Name, Age, Grade, Subject, Score)
import pandas as pd
read=pd.read_csv('students.csv')
print(read.head())
