import os
import json

import errors


def get_non_recurring_items(l1: list, l2: list) -> list:
    return [i for i in l1 if i not in l2]


def log_warn(msg: str, end='\n') -> None:
    print(f'\n[WARN]: {msg}', end=end)


def log_error(msg: str, end='\n') -> None:
    print(f'[ERROR]: {msg}', end=end)


def log_info(msg: str, end='') -> None:
    print(f'\r[INFO]: {msg}', end=end)


def read_file(path: str, mode: str):
    if file_is_exists(path) == False:
        return errors.FILE_NOT_EXISTS
    if mode not in ('r', 'rb'):
        return errors.INVALID_READ_MODE
    return open(path, mode).read()


def get_all_chunk_coords_from_region(path: str) -> int|tuple:
    if file_is_exists(path) == False:
        return errors.FILE_NOT_EXISTS
    if is_dir(path):
        return errors.ITS_NOT_FILE

    result = []

    file = open(path, 'rb')
    for ch_z in range(32):
        for ch_x in range(32):
            offset_and_sector_count = int.from_bytes(file.read(4), 'big')
            if offset_and_sector_count != 0:
                result.append((ch_x, ch_z))
    file.close()

    return tuple(result)


def file_is_exists(path: str) -> bool:
    return os.path.exists(path)


def is_file(path: str) -> bool:
    return os.path.isfile(path)


def is_dir(path: str) -> bool:
    return os.path.isdir(path)


def get_file_type(path: str) -> str:
    return os.path.splitext(path)[1]


def concatenate_paths(path1: str, path2: str) -> str:
    return os.path.join(path1, path2)


def get_all_file_names(path: str) -> list:
    return os.listdir(path)
