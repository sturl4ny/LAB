import json
import pandas as pd

file = r"D:\_Lab\Git\LAB-1\JSON\Permission_and_role copy.json"

with open(file, 'r') as f:
    json = json.load(f)

df = pd.DataFrame(json['assignments'])
users = df['user-or-group']
split = df.explode('user-or-group')
duplicated = df.duplicated('object')

#df = pd.json_normalize(json)
# 4. Display the result
print(df)
#print(users)
#print(split)
print(duplicated)
