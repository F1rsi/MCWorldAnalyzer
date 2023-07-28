import sys, os, json

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
        rg = anvil.Region.from_file(os.path.join(os.path.join(world_path, DIM_PATH), rg_name))
        rg_result = b_map

        print(f'Started new region: {rg_name}')

        for cx in range_RGSIZE:
            for cz in range_RGSIZE:

                c = anvil.Chunk.from_region(rg, cx, cz)
                if c is None:
                    print(f'Skiped chunk at x:{cx} z:{cz}')
                    continue

                print(f'Processed chunk at x:{cx} z:{cz}')

                for by in range_CHEIGHT:
                    for bx in range_CWIDTH:
                        for bz in range_CLENGTH:

                            b = c.get_block(bx, by, bz)

                            try:
                                rg_result[b.id][b.data] += 1
                            except IndexError:
                                print(f'KeyError: {b.data} for {b.id}')
                                exit()

        print(f'Save result data for "{rg_name}"')

        with open(os.path.join(output_dir_path, os.path.splitext(rg_name)[0] + '.json'), 'w') as f:
            json.dump(rg_result, f, indent=3)

    
world_path = sys.argv[1]
output_dir_path = sys.argv[2]
dimension = sys.argv[3]

main(world_path, output_dir_path, dimension)
