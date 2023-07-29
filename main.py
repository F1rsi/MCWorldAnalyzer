import sys
import os
import json
import time

import anvil


def main(world_path: str, output_dir_path: str, dimension: int):
    DIM_PATH = 'region'
    if dimension == 1:
        DIM_PATH = 'DIM1/region'
    elif dimension == -1:
        DIM_PATH = 'DIM-1/region'

    b_map = json.load(open('b_map.json'))

    CHEIGHT = 256
    CWIDTH = 16
    CLENGTH = 16

    RGSIZE = 32

    range_CWIDTH = range(CWIDTH)
    range_CLENGTH = range(CLENGTH)
    range_CHEIGHT = range(CHEIGHT)
    range_RGSIZE = range(RGSIZE)

    if not os.path.exists(output_dir_path):
        print('Create output directory.')
        os.makedirs(output_dir_path)
        rgs_processed = []
    else:
        rgs_processed = [i.replace('.json', '.mca') for i in os.listdir(output_dir_path)]

    rgs = os.listdir(os.path.join(world_path, DIM_PATH))
    rgs = [i for i in rgs if i not in rgs_processed]

    for rg_name in rgs:
        time_begin = time.time()

        rg = anvil.Region(os.path.join(os.path.join(world_path, DIM_PATH), rg_name))
        #if anvil.utils.get_chunk_count_from_rg()

        rg_result = b_map

        c_processed = 0

        print(f'Started new region: {rg_name}')

        for cx in range_RGSIZE:
            for cz in range_RGSIZE:

                c_processed += 1
                c = anvil.Chunk.from_region(rg, cx, cz)
                if c is None:
                    print(f'Skiped chunk at x:{cx} z:{cz}')
                    continue

                print(f'\rProcessed chunk at x:{cx} z:{cz}; Progress: {c_processed / 1024 * 100}%\t', end='')

                for by in range_CHEIGHT:
                    for bx in range_CWIDTH:
                        for bz in range_CLENGTH:

                            b = c.get_block(bx, by, bz)
                            rg_result[b.id][b.data] += 1

        time_end = time.time()

        print(f'\nSave result data for "{rg_name}"')
        print(f'Time elapsed: {int(time_end - time_begin)}s')

        with open(os.path.join(output_dir_path, os.path.splitext(rg_name)[0] + '.json'), 'w') as f:
            json.dump(rg_result, f, indent=3)

    
world_path = sys.argv[1]
output_dir_path = sys.argv[2]
dimension = sys.argv[3]

main(world_path, output_dir_path, dimension)
