import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-paper')

df = pd.read_csv('./data/df_funnel.csv', index_col=0)
# print(df.info())
# print(df.head(5))

# print(df.groupby("datetime").size().head(15))
df['datetime'] = pd.to_datetime(df['datetime'])
# print(df.info())
# print(df.head(5))

