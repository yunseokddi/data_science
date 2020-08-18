import pandas as pd

friend_list = [
    {'name': 'John', 'age': 20, 'job': 'student'},
    {'name': 'Jenny', 'age': 30, 'job': 'developer'},
    {'name': 'nate', 'age': 30, 'job': 'teacher'}
]

df = pd.DataFrame(friend_list)
df = df[['name', 'age', 'job']]

# print(df[1:3])

#load method
# df = df[1:3]
# print(df)

#specific index
# print(df.loc[[0,2]])

#by column condition

# print(df[df.age >25])
# print(df.query('age>25'))

# print(df[(df.age>25)&(df.name=='nate')])


#Filter Column
#by index

# print(df.iloc[:, 0:2]) #first index: row, second index: column

# print(df.iloc[0:2, 0:2])

#by column name
df = pd.read_csv('./data/friend_list_no_head.csv', header=None, names=['name', 'age','job'])
df_filtered = df[['name', 'age']]
# print(df_filtered)
# print('==============')
#
# print(df.filter(items=['age', 'job']))

# print(df.filter(like='a', axis=1))

# print(df.filter(regex='b$', axis=1))

