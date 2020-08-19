import pandas as pd
import numpy as np

# date_list = [{'date':'2000-06-27'},
#              {'date':'2002-09-24'},
#              {'date':'2005-12-20'}]
#
# df = pd.DataFrame(date_list, columns=['date'])
#
# def extract_year(date):
#     return date.split('-')[0]

# df['year'] = df['date'].apply(extract_year)

# people_list = [{'age': 20, 'job': 'student'},
#                {'age': 30, 'job': 'developer'},
#                {'age': 30, 'job': 'teacher'}]
#
# df = pd.DataFrame(people_list)
#
# df.job = df.job.map({'student':1, 'developer':2, 'teacher':3})
#

x_y = [{'x': 5.5, 'y':-5.6, 'z':-1.1},
       {'x': -5.2, 'y':5.5, 'z':-2.2},
       {'x': -1.6, 'y':-4.5, 'z':-3.3}]

df = pd.DataFrame(x_y)

df = df.applymap(np.around)
print(df)