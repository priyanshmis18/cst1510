"""
RECORD CHECK  -  my version
===========================

Name  : priyansh mishra
Lane  :  AI 
Date  : 18-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Farhat\Downloads\mdx\Week 06\Week 06 - Pandas\Week 06 - Pandas\LAB\records_sample.csv")
df['percent'] = (df['value']/ df['limit']) * 100

df['status'] = df['percent'].apply(
    lambda p: 'OVER LIMIT' if p >= 100 else ('WARNING' if p >= 90 else 'OK')
)
print(df)

print("ROWS THAT ARE NOT OK")
print(df[df['status'] !='OK'])

print("COUNT PER STATUS GROUP")
print(df['status'].value_counts())
df.to_csv("records_report.csv", index=False)
df['status'].value_counts().plot(kind="bar",title="servers by status")
plt.tight_layout()
plt.savefig("status_counts.png")
plt.show()


