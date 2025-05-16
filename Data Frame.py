import pandas as pd
df1=pd.DataFrame({'key':['A','B','C'], 'value':[1,2,3]})
df2=pd.DataFrame({'key':['D','E','F'], 'value':[4,5,6]})
df1
#Renaming columns
display(df1)
df1.columns=['Alphabet','Numeric Value']
display(df1)
df1.drop('Alphabet',axis=1,inplace=True)

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('processed_students.csv')
plt.scatter(df['Age'], df['Score'], color='blue')
plt.xlabel('Age')
plt.ylabel('Score')
plt.title('Relationship Between Age and Score')
plt.show()
