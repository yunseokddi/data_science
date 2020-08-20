import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
plt.style.use('seaborn-paper')

df = pd.read_csv('./data/df_funnel.csv', index_col=0)

# 2-1) 날짜를 pandas datetime으로 변환

# case 1. if date type is string
# str_date = ['2018/01/01', '2018.01.02', '2018-01-03', '2018-01-04', '2018/01/05']
# print(pd.to_datetime(str_date)) #to parsed
# print(pd.Series(pd.to_datetime(str_date)))

# case 2. if date type is timestamp
# print(pd.Series(pd.to_datetime([1530837876, 1530751476, 1530665076, 1530578676, 1530492276], unit='s')).dt.date)

# case 3. when changing column type only
# print(df.info())
# print(df.head())

# option 1
# print(df['datetime'].astype('datetime64[ns]').head())
# option 2
# print(pd.to_datetime(df['datetime']).head())

# day to year
# print(df['datetime'].dt.year[:10])
# day to month
# print(df['datetime'].dt.month[:10])
# day to day
# print(df['datetime'].dt.day[:10])


# 2-2) Missing value check
# df['datetime'] = pd.to_datetime(df['datetime'])
# print(df.info())
# print(df.isnull().sum())


# 2-3) 결측치 처리
# 결측치가 하나 이상 존재시 행 삭제
# df.dropna()

# 모든 값이 null일 경우 행 삭제
# df.dropna(how='all')

# 결측치가 하나 이상 있는 case만 선택
# df[df.isnull().any(axis=1)]

# df_by_screen = df.groupby(["datetime", "screen"])['sessionid'].nunique().unstack()
# print(df_by_screen.isnull().sum())
# print(df_by_screen.info())
# print(df_by_screen.fillna(0)[:10])

# dropna with 'how' param
# print(df_by_screen.dropna(how='any')[:10])
# print(df_by_screen.dropna(how='all')[:10])

# select only rows, including NaN
# print(df_by_screen[df_by_screen.isnull().any(axis=1)])

# fill NaN with median
# print(df_by_screen.fillna(df_by_screen.median())[:10])

# 2-5) 확장자명 통일
# print(df.ext.value_counts())

# ext_dic = {'DOCX': 'DOC',
#            'XLSX': 'XLS',
#            'PPTX': 'PPT',
#            'PPSX': 'PPT',
#            'PPS': 'PPT',
#            'ODT': 'TXT',
#            'PNG': 'JPG'}
#
# df['ext'] = df['ext'].replace(ext_dic)
# print(df['ext'].value_counts())

# 2-6) Action Type 통일
# print(df.actiontype.value_counts())


