import pandas as pd
df1=pd.DataFrame({'key':['A','B','C'], 'value':[1,2,3]})
df2=pd.DataFrame({'key':['D','E','F'], 'value':[4,5,6]})
df1
#Renaming columns
display(df1)
df1.columns=['Alphabet','Numeric Value']
display(df1)