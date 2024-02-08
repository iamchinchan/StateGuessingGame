import pandas as pd
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', None],
        'age': [25, 32, 18, 47, 22]}
data = pd.DataFrame(data)
# print(data)
# data["name"]   =data['name'].str.lower()
# print(data)
# print(data["name"])
# for name in data["name"].to_list():
#   print(name)
# print(data["name"].str.lower())
# if 'alice' in data["name"].str.lower().to_list(): 
#   print("found")  
# else:
#   print("not found")
# print(data)

names=["Jatin","Goyal"]

if "Jatin" in [x.lower() for x in names]:
  print("found")
else:
  print("not found")