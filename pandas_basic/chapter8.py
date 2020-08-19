import pandas as pd

# student_list = [{'name': 'John', 'major': 'Computer Science', 'sex': 'male'},
#                 {'name': 'Nate', 'major': 'Computer Science', 'sex': 'male'},
#                 {'name': 'Abraham', 'major': 'Physics', 'sex': 'male'},
#                 {'name': 'Brian', 'major': 'Psychology', 'sex': 'male'},
#                 {'name': 'John', 'major': 'Computer Science', 'sex': 'male'}
#                 ]
#
# df = pd.DataFrame(student_list, columns=['name', 'major', 'sex'])

#unique
# print(df.drop_duplicates())

student_list = [{'name': 'John', 'major': 'Computer Science', 'sex': 'male'},
                {'name': 'Nate', 'major': 'Computer Science', 'sex': 'male'},
                {'name': 'Abraham', 'major': 'Physics', 'sex': 'male'},
                {'name': 'Brian', 'major': 'Psychology', 'sex': 'male'},
                {'name': 'John', 'major': 'Psychology', 'sex': 'male'}
                ]

df = pd.DataFrame(student_list, columns=['name', 'major', 'sex'])

print(df.drop_duplicates(['name'], keep='last'))