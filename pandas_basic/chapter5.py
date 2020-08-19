import pandas as pd

# friends = [{'age': 15, 'job': 'student'},
#            {'age': 25, 'job': 'developer'},
#            {'age': 30, 'job': 'teacher'}]
#
# df = pd.DataFrame(friends,
#                   index=['John', 'Jenny', 'Nate'],
#                   columns=['age', 'job'])

# delete - 1 (drop)
# df = df.drop(['John', 'Nate'])
# print(df)

# delete - 1 (inplace)
# df.drop(['John', 'Nate'], inplace=True)
# print(df)

friends = [{'name': 'John', 'age': 15, 'job': 'student'},
           {'name': 'Ben', 'age': 25, 'job': 'developer'},
           {'name': 'Jenny', 'age': 30, 'job': 'teacher'}]

df = pd.DataFrame(friends,
                  columns=['name', 'age', 'job'])

# delete using index
#
# df = df.drop(df.index[[0, 2]])
#
# print(df)

# delete using column value
#
# df = df[df.age > 20]
# print(df)

#delete column
df.drop('age', axis=1, inplace=True)
print(df)