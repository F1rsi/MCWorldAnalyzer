import os


def get_chunk_count_from_rg(rg_name: str) -> int:
    if not os.path.exists(rg_name):
        return -1
    with open(rg_name, 'rb') as f:
        chunk_count = 0
        for i in range(1024):
            if int.from_bytes(f.read(4), 'big'):
                chunk_count += 1
        return chunk_count
