import pandas as pd
import numpy as np

# friends = [{'name': 'John', 'age': 15, 'job': 'student'},
#            {'name': 'Ben', 'age': 25, 'job': 'developer'},
#            {'name': 'Jenny', 'age': 30, 'job': 'teacher'}]
#
# df = pd.DataFrame(friends,
#                   columns=['name', 'age', 'job'])

# insert column
# df['salary'] = 0
#
# df['salary'] = np.where(df['job'] != 'student', 'yes', 'no')
#

friends = [{'name': 'John', 'midterm': 95, 'final': 85},
           {'name': 'Ben', 'midterm': 85, 'final': 80},
           {'name': 'Jenny', 'midterm': 30, 'final': 10}]

df = pd.DataFrame(friends,
                  columns=['name', 'midterm', 'final'])

# df['total'] = df['midterm'] + df['final']
# df['avg'] = df['total'] / 2
#
# grades = []
#
# for row in df['avg']:
#     if row >= 90:
#         grades.append('A')
#
#     elif row >= 80:
#         grades.append('B')
#
#     else:
#         grades.append('F')
#
# df['grade'] = grades
#
#
# def pass_or_fail(row):
#     if row != 'F':
#         return 'Pass'
#
#     else:
#         return 'Fail'
#
#
# df.grade = df.grade.apply(pass_or_fail)
#
# date_list = [
#     {
#         'yyyy-mm-dd': '2000-06-27'
#     },
#     {
#         'yyyy-mm-dd': '2007-10-27'
#     }
# ]
#
# df = pd.DataFrame(date_list, columns=['yyyy-mm-dd'])
#
# def extract_year(row):
#     return row.split('-')[0]
#
# df['year'] = df['yyyy-mm-dd'].apply(extract_year)
# print(df)

#insert row
df2 = pd.DataFrame([
    ['Ben', 50, 50]
], columns=['name', 'midterm', 'final'])

df = df.append(df2, ignore_index=True)

print(df)