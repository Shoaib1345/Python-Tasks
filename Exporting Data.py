import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('processed_students.csv')
subject_counts = df['Subject'].value_counts()
plt.figure(figsize=(8, 5))
subject_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Students per Subject')
plt.xlabel('Subjects')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
