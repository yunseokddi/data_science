import pandas as pd

l1 = [{'name': 'John', 'job': 'teacher'},
      {'name': 'Nate', 'job': 'student'},
      {'name': 'Fred', 'job': 'developer'}]

l2 = [{'name': 'Ed', 'job': 'dentist'},
      {'name': 'Jack', 'job': 'farmer'},
      {'name': 'Ted', 'job': 'designer'}]

l3 = [{'name': 'John', 'job': 'teacher'},
      {'name': 'Nate', 'job': 'student'},
      {'name': 'Jack', 'job': 'developer'}]

l4 = [{'age': 25, 'country': 'US'},
      {'age': 30, 'country': 'UK'},
      {'age': 45, 'country': 'Korea'}]

df1 = pd.DataFrame(l1, columns=['name', 'job'])
df2 = pd.DataFrame(l2, columns=['name', 'job'])

# union method 1
result = pd.concat([df1, df2], ignore_index=True)

# union method 2
result = df1.append(df2, ignore_index=True)

df1 = pd.DataFrame(l3, columns=['name', 'job'])
df2 = pd.DataFrame(l4, columns=['age', 'country'])

# row union method
result = pd.concat([df1, df2], axis=1, ignore_index=True)

# list union method
label = [1, 2, 3, 4, 5]
prediction = [1, 2, 2, 4, 4]

compariosion = pd.DataFrame({'label':label, 'prediction': prediction})
print(compariosion)