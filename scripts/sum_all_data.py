import os, json


result = {}
for file_name in os.listdir('result'):
    data = {i.split('=')[0]: int(i.split('=')[1]) for i in open(os.path.join('result', file_name)).read().split('\n') if i}
    for key in data.keys():
        try:
            result[key] += data[key]
        except KeyError:
            result[key] = data[key]

print(result)

with open('result.json', 'w') as f:
    json.dump(result, f, indent=3)
