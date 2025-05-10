import pandas as pd
read = pd.read_csv('students.csv')
reslut=[]
for score in read['Score']:
    if score>=50:
        reslut.append('Pass')
    else:
        reslut.append('Fail')
read['Result']=reslut

read.to_csv('processed_students.csv', index=False)
print(read)