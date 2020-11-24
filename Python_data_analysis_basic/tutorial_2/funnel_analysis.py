import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
from sklearn.metrics import classification_report

plt.style.use('seaborn-paper')

df = pd.read_csv('./data/df_funnel.csv', index_col=0)
# print(df.info())
# print(df.head(5))

# print(df.groupby("datetime").size().head(15))
df['datetime'] = pd.to_datetime(df['datetime'])
# print(df.info())
# print(df.head(5))

# print(df.isnull().sum())

# pandas의 fillna()를 통해 NULL값을 채우는 것이 가능

# df_by_screen = df.groupby(["datetime", "screen"])['sessionid'].nunique().unstack()
# print(df_by_screen[:10])
# print(df_by_screen.isnull().sum())

# 결측치를 0으로 처리
# print(df_by_screen.fillna(0)[:10])

# 결측치 버리기, how = any, all
# print(df_by_screen.dropna(how='any')[:10])

# NULL을 포함한 ROW만 선택
# print(df_by_screen[df_by_screen.isnull().any(axis=1)])

# NULL 값을 중앙값으로 채우기
# print(df_by_screen.fillna(df_by_screen.median())[:10])

# --------------------결측치가 카테고리 변수인 경우--------------------
# df_ms = df.copy()
# df_ms.loc[2, 'documentposition'] = np.nan
# df_ms.loc[5, 'documentposition'] = np.nan
# df_ms.loc[7, 'documentposition'] = np.nan
# df_ms.loc[10, 'documentposition'] = np.nan
# df_ms.loc[11, 'documentposition'] = np.nan
# df_ms.loc[15, 'documentposition'] = np.nan

# print(df_ms.head(10))

# table 빈도
# print(df_ms.documentposition.value_counts())

# freq_values = df_ms.documentposition.value_counts().index[0]

# NULL값을 최빈값으로 채우기
# df_ms['documentposition'] = df_ms['documentposition'].fillna(freq_values)
# print(df_ms.head(10))

# fill na using predictive model
# df_msl = df_ms.dropna()
#
# ind_cols = ['actiontype', 'ismydoc', 'ext', 'screen']
#
# x = df_msl[ind_cols]
# y = df_msl[['documentposition']]
# # print(x.head(10))
# # print(y[:10])
#
# encoder = LabelEncoder()
# #
# x = x.apply(lambda x: encoder.fit_transform(x))
# y = y.apply(lambda y: encoder.fit_transform(y))
#
# # print(x.head(10))
# # print(y[:10])
#
# x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=10)
#
# # print(x.shape)
# # print(y.shape)
#
# KNN = KNeighborsClassifier(n_neighbors=5).fit(x_train,y_train)
#
# # print(KNN.score(x_train, y_train))
# # print(KNN.score(x_test, y_test))
#
# # knn_pred =KNN.predict(x_test)
# # print(knn_pred[:20])
# # print('-'*10)
# # print(confusion_matrix(y_test, knn_pred))
# # print('-'*10)
# # print(classification_report(y_test, knn_pred))
#
# # print(pd.Series(knn_pred).value_counts().sort_index())
# # print('-'*10)
# class_cd = pd.Series(encoder.classes_).to_dict()
# # print(class_cd)
#
# df_ms_only = df_ms[df_ms.isnull().any(axis=1)]
# # print(df_ms_only)
# #
# df_ms_dropna = df_ms.dropna()
# # print(df_ms_dropna.head())
#
# fill_na_values = KNN.predict(df_ms_only[ind_cols].apply(lambda  x: encoder.fit_transform(x)))
#
# df_ms_only['documentposition'] = fill_na_values
# # print(df_ms_only.head(10))
# df_ms_only['documentposition'] = df_ms_only['documentposition'].replace(class_cd)
# # print(df_ms_only.head(10))
#
# df_ms_final = pd.concat([df_ms_dropna, df_ms_only], axis=0)
# print(df_ms_final.head(10))

# --------------------확장자명 통일-----------------------
# print(df.head(10))
# print(df.ext.value_counts())
#
#
ext_dic = {'DOCX': 'DOC',
           'XLSX': 'XLS',
           'PPTX': 'PPT',
           'PPSX': 'PPT',
           'PPS': 'PPT',
           'ODT': 'TXT',
           'PNG': 'JPG'}
#
df['ext'] = df['ext'].replace(ext_dic)
# print(df.ext.value_counts())

# --------------------Action Type 통일-----------------------
act_dic = {'SAVEAS': 'SAVE',
           'SAVEAS_OTHER': 'SAVE',
           'EXPORT_SAME': 'EXPORT'
           }

df['actiontype'] = df['actiontype'].replace(act_dic)

# --------------------신규 session_id 부여-----------------------
s = []
j = 0

for i in range(len(df) - 1):
    if df.loc[i, 'sessionid'] == df.loc[i + 1, 'sessionid']:
        s.append(j)
    else:
        s.append(j)
        j += 1

df['sessionid'] = pd.Series(['sess' + str(x) for x in s])

# --------------------EDA-----------------------
# showing data time
# df.groupby("datetime").size().plot(c='r')
# plt.title("Daily Log Count")
# plt.grid(color='lightgrey', alpha=0.5, linestyle='--')
# plt.tight_layout()
# plt.show()

# showing daily session
# df.groupby("datetime")['sessionid'].nunique().plot(c='b')
# plt.title("Daily Session")
# plt.grid(color='lightgrey', alpha=0.5, linestyle='--')
# plt.tight_layout()
# plt.show()

# -----------------------------------------------
# s = df.groupby("datetime")["sessionid"].nunique()
# s.index = s.index.dayofweek
#
# s.plot(color='grey', kind='bar', rot=0)
#
# plt.title('Daily Session')
# plt.grid(color='lightgrey', alpha=0.5, linestyle='--')
# plt.tight_layout()
# plt.show()

# -----------------------------------------------
# df.groupby(["datetime", "ext"]).size().unstack().dropna(axis=1).plot(figsize=(12,7))
#
# plt.title("Daily Extention Trend")
# plt.grid(color='lightgrey', alpha=0.5, linestyle='--')
# plt.tight_layout()
# plt.show()

# -----------------------------------------------
# df.groupby(["datetime", "screen"]).size().unstack().fillna(0) .astype(int).plot(figsize=(12,7))
#
# plt.title("Daily screens")
# plt.grid(color='lightgrey', alpha=0.5, linestyle='--')
# plt.tight_layout()

# -----------------------------------------------
screens = df.groupby(["datetime", "screen"])['sessionid'].nunique().unstack().fillna(0).astype(int)

screens = screens[screens.mean().sort_values(ascending=False).index]
# print(screens[:10])

plt.subplots(figsize=(17, 8))

sns.heatmap(screens, annot=True, fmt="d", annot_kws={"size": 12}, cmap='Blues');

plt.title("screen count daily")
plt.tight_layout()
plt.show()

# --------------------Pivoting을 통한 변수별 특성 탐색-----------------------
