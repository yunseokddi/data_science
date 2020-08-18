import pandas as pd

#method 1 (using dict)
# friend_dict_list = [
#     {'name': 'John', 'age': 25, 'job': 'student'},
#     {'name': 'Nate', 'age': 30, 'job': 'teacher'}
# ]
#
# df = pd.DataFrame(friend_dict_list)
# print(df.head())

# df = df[['name', 'age', 'job']]
# print(df.head())

#method 2 (using OrderedDict)
# from collections import OrderedDict
#
# friend_ordered_dic = OrderedDict(
#     [
#         ('name', ['John', 'Nate']),
#         ('age', ['25', '30']),
#         ('job', ['Student', 'Teacher'])
#     ]
# )
#
# df = pd.DataFrame.from_dict(friend_ordered_dic)
#
# print(df.head())

#method 3-1 (using list)
# friend_list = [
#     ['John', 20, 'Student'],
#     ['Nate', 30, 'teacher']
# ]
#
# column_name = ['name', 'age', 'job']
#
# df = pd.DataFrame.from_records(friend_list, columns=column_name)
# print(df.head())

#method 3-2 (using list)
# friend_list = [
#     ['name', ['John', 'Nate']],
#     ['age', [20, 30]],
#     ['job', ['student', 'teacher']]
# ]
# df = pd.DataFrame.from_items(friend_list)
# print(df.head)