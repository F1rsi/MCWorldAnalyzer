# Warning, you need firstly run sum_all_result_data.py

from sys import argv
from json import load
from os import listdir, path


def count_all_chunks_from_region(path: str) -> int|tuple:
    result = 0

    file = open(path, 'rb')
    for ch_z in range(32):
        for ch_x in range(32):
            offset_and_sector_count = int.from_bytes(file.read(4), 'big')
            if offset_and_sector_count != 0:
                result += 1
    file.close()

    return result


input_path_for_all_result_data = argv[1]
input_path_for_region_files = argv[2]

result_data = load(open(input_path_for_all_result_data))
block_count = sum(result_data.values())
chunk_count = 0

for file_name in listdir(input_path_for_region_files):
    if path.splitext(file_name)[-1] == '.mca':
        chunk_count += count_all_chunks_from_region(path.join(input_path_for_region_files, file_name))

print(block_count == chunk_count * 16 * 16 * 256)
