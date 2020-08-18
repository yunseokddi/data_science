import pandas as pd

friend_dict_list = [
    {'name': 'John', 'age': 25, 'job': 'student'},
    {'name': 'Nate', 'age': 30, 'job': 'teacher'},
    {'name': 'Jenny', 'age': 30, 'job': None}
]

df = pd.DataFrame(friend_dict_list)
df = df[['name', 'age', 'job']]

df.to_csv('friends.csv', index=True, header=True, na_rep='-')