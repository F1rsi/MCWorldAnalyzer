import sys, os, json

import anvil


def main(world_path: str, output_file_path: str, dimension: int):
    DIM_PATH = 'region'
    if dimension == 1:
        DIM_PATH = 'DIM1/region'
    elif dimension == -1:
        DIM_PATH = 'DIM-1/region'
    
    b_map = json.load(open('b_map.json'))

    CHEIGHT = 256
    CWIDTH = 16
    CLENGTH = 16

    range32 = range(32)
    range_CHEIGHT = range(CHEIGHT)
    range_CWIDTH = range(CWIDTH)
    range_CLENGTH = range(CLENGTH)
    
    rgs = os.listdir(os.path.join(world_path, DIM_PATH))
    rgs = [os.path.join(os.path.join(world_path, DIM_PATH), i) for i in rgs]
    
    for rg_name in rgs:
        rg = anvil.Region.from_file(rg_name)
        
        print(f'Started new region: {rg_name}')
        
        for cx in range32:
            for cz in range32:
                
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
                                b_map[b.id][b.data] += 1
                            except IndexError:
                                print(f'KeyError: {b.data} for {b.id}')
                                exit()
    
    with open(output_file_path, 'w') as f:
        json.dump(b_map, f, indent=3)

    
world_path = sys.argv[1]
output_file_path = sys.argv[2]
dimension = sys.argv[3]

main(world_path, output_file_path, dimension)

