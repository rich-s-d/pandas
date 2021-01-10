# PANDAS/practice.py

import pandas as pd

fp = r"/home/parallels/Downloads/FL_insurance_sample.csv"
data = pd.read_csv(fp)
# print(data.head)
print(data.shape)