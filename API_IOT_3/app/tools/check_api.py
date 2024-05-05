import requests as r
import json
url = "http://127.0.0.1:8000/api/entity/"

data = r.get(url)
cont = data.content


data = json.loads(cont)

for i in range(len(data)):
  print(data[i]['entiy_id'])
  print(data[i]['type_id'])
  print(data[i]['role_id'])
  print(data[i]['entity_type'])
  print(data[i]['entity_role'])
  print(data[i]['name'])
  print(data[i]['short_name'])
  print(data[i]['long_name'])
  print(data[i]['trade_name'])
  print("\n\n")


