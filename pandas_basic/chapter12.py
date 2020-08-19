import pandas as pd

school_id_list = [{'name': 'John', 'job':'teacher', 'age':40},
                  {'name': 'Nate', 'job':'teacher', 'age':35},
                  {'name': 'Yuna', 'job':'teacher', 'age':37},
                  {'name': 'Abrham', 'job':'student', 'age':10},
                  {'name': 'Brian', 'job':'student', 'age':12},
                  {'name': 'Jenny', 'job':'student', 'age':11},
                  {'name': 'Nate', 'job':'teacher', 'age':None},
                  {'name': 'John', 'job':'student', 'age':None}
                  ]

df = pd.DataFrame(school_id_list,columns=['name', 'job'])

print(df.job.value_counts())