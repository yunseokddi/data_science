import pandas as pd

date_list = [{'yyyy-mm-dd': '2000-06-27'},
             {'yyyy-mm-dd': '2002-09-24'},
             {'yyyy-mm-dd': '2005-12-20'}]

df = pd.DataFrame(date_list, columns=['yyyy-mm-dd'])

def extract_year(colum):
    return colum.split('-')[0]

df['year'] = df['yyyy-mm-dd'].apply(extract_year)

def get_age(year, current_year):
    return current_year - int(year)

df['age'] = df['year'].apply(get_age, current_year=2020)


def get_introduce(age, prefix, suffix):
    return prefix+str(age)+suffix

df['introduce'] = df['age'].apply(get_introduce, prefix='I am ', suffix=' years old')


def get_introduce2(row):
    return 'I was born in '+str(row.year)+' my age is ' + str(row.age)

df['introduce2'] = df.apply(get_introduce2, axis=1)
print(df)