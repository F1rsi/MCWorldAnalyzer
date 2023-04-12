from os import listdir, path
from sys import argv
from json import dump


input_path = argv[1]
output_path = argv[2]
if not path.exists(input_path):
    print(f'Path "{input_path}" does not exists!')
    exit(1)

result = {}
for file_name in listdir(input_path):
    data = {i.split('=')[0]: int(i.split('=')[1]) for i in open(path.join(input_path, file_name)).read().split('\n') if i}
    for key, value in data.items():
        try:
            result[key] += value
        except KeyError:
            result[key] = value

with open(path.join(output_path, 'result.json'), 'w') as f:
    dump(result, f, indent=3)

