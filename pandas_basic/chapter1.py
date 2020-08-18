import pandas as pd

#read csv file
# df = pd.read_csv('./data/friend_list.csv')

#print data_frame
# print(df)
# print(df.head())
# print(df.head(2))
# print(df.tail())
# print(df.tail(3))

#read txt file
# df = pd.read_csv('./data/friend_list.txt')
# print(df)

#read tap txt file
# df = pd.read_csv('./data/friend_list_tab.txt', delimiter='\t')
# print(df)

#read no head txt file - 1
# df = pd.read_csv('./data/friend_list_no_head.csv', header=None)
# df.columns = ['name', 'age', 'job']
# print(df)

#read no head txt file - 2
# df = pd.read_csv('./data/friend_list_no_head.csv', header=None, names=['name', 'age', 'job'])
# print(df)