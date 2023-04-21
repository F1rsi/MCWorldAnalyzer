import sys
import argparse

from utils import *
import anvil


def main(args):
    CHUNK_HEIGHT = 256
    CHUNK_WIDTH = 16
    CHUNK_LENGTH = 16

    # For more optimization.
    CHUNK_HEIGHT_RANGE = range(CHUNK_HEIGHT)
    CHUNK_WIDTH_RANGE = range(CHUNK_WIDTH)
    CHUNK_LENGTH_RANGE = range(CHUNK_LENGTH)

    path_to_regions = concatenate_paths(args.input, 'region')
    region_file_names = get_all_file_names(path_to_regions)
    
    OUTPUT_FOLDER = args.output
    OUTPUT_USED_REGION_FILE_NAMES = concatenate_paths(OUTPUT_FOLDER, 'used_region_file_names.txt')

    if file_is_exists(OUTPUT_USED_REGION_FILE_NAMES):
        used_region_file_names = open(OUTPUT_USED_REGION_FILE_NAMES).read().split('\n')
    else:
        used_region_file_names = []

    unused_region_file_names = get_non_recurring_items(region_file_names, used_region_file_names)
    for region_file_name in unused_region_file_names:
        log_info(f'Start new region: "{region_file_name}"', end='\n')

        block_acacia_door = 0
        block_acacia_fence = 0
        block_acacia_leaves = 0
        block_acacia_log = 0
        block_acacia_planks = 0
        block_acacia_stairs = 0
        block_air = 0
        block_allium = 0
        block_andesite = 0
        block_azure_bluet = 0
        block_bed = 0
        block_bedrock = 0
        block_beetroots = 0
        block_birch_fence = 0
        block_birch_leaves = 0
        block_birch_log = 0
        block_birch_planks = 0
        block_birch_slab = 0
        block_birch_stairs = 0
        block_black_carpet = 0
        block_black_wool = 0
        block_blue_carpet = 0
        block_blue_orchid = 0
        block_blue_terracotta = 0
        block_blue_wool = 0
        block_bone_block = 0
        block_bookshelf = 0
        block_brewing_stand = 0
        block_brown_carpet = 0
        block_brown_mushroom = 0
        block_brown_mushroom_block = 0
        block_brown_terracotta = 0
        block_brown_wool = 0
        block_cactus = 0
        block_carrots = 0
        block_carved_pumpkin = 0
        block_cauldron = 0
        block_chest = 0
        block_chiseled_sandstone = 0
        block_chiseled_stone_bricks = 0
        block_clay = 0
        block_coal_ore = 0
        block_coarse_dirt = 0
        block_cobblestone = 0
        block_cobblestone_slab = 0
        block_cobblestone_stairs = 0
        block_cobblestone_wall = 0
        block_cobweb = 0
        block_cocoa = 0
        block_cracked_stone_bricks = 0
        block_crafting_table = 0
        block_cut_sandstone = 0
        block_cyan_carpet = 0
        block_cyan_wool = 0
        block_dandelion = 0
        block_dark_oak_fence = 0
        block_dark_oak_fence_gate = 0
        block_dark_oak_leaves = 0
        block_dark_oak_log = 0
        block_dark_oak_planks = 0
        block_dark_oak_sapling = 0
        block_dark_oak_stairs = 0
        block_dark_prismarine = 0
        block_dead_bush = 0
        block_dead_shrub = 0
        block_diamond_block = 0
        block_diamond_ore = 0
        block_diorite = 0
        block_dirt = 0
        block_dispenser = 0
        block_emerald_ore = 0
        block_end_portal_frame = 0
        block_farmland = 0
        block_fern = 0
        block_flower_pot = 0
        block_furnace = 0
        block_glass = 0
        block_glass_pane = 0
        block_gold_ore = 0
        block_granite = 0
        block_grass = 0
        block_grass_block = 0
        block_grass_path = 0
        block_gravel = 0
        block_gray_carpet = 0
        block_gray_wool = 0
        block_green_carpet = 0
        block_green_wool = 0
        block_ice = 0
        block_infested_chiseled_stone_bricks = 0
        block_infested_cobblestone = 0
        block_infested_cracked_stone_bricks = 0
        block_infested_mossy_stone_bricks = 0
        block_infested_stone = 0
        block_infested_stone_bricks = 0
        block_iron_bars = 0
        block_iron_door = 0
        block_iron_ore = 0
        block_jungle_leaves = 0
        block_jungle_log = 0
        block_ladder = 0
        block_lapis_block = 0
        block_lapis_ore = 0
        block_large_fern = 0
        block_lava = 0
        block_lever = 0
        block_light_blue_carpet = 0
        block_light_blue_wool = 0
        block_light_gray_carpet = 0
        block_light_gray_terracotta = 0
        block_light_gray_wool = 0
        block_lilac = 0
        block_lily_pad = 0
        block_lime_carpet = 0
        block_lime_wool = 0
        block_magenta_carpet = 0
        block_melon = 0
        block_melon_stem = 0
        block_mossy_cobblestone = 0
        block_mossy_cobblestone_wall = 0
        block_mossy_stone_bricks = 0
        block_mycelium = 0
        block_oak_door = 0
        block_oak_fence = 0
        block_oak_leaves = 0
        block_oak_log = 0
        block_oak_planks = 0
        block_oak_pressure_plate = 0
        block_oak_sign = 0
        block_oak_slab = 0
        block_oak_stairs = 0
        block_oak_trapdoor = 0
        block_obsidian = 0
        block_orange_carpet = 0
        block_orange_terracotta = 0
        block_orange_tulip = 0
        block_orange_wool = 0
        block_oxeye_daise = 0
        block_packed_ice = 0
        block_peony = 0
        block_pink_carpet = 0
        block_pink_tulip = 0
        block_podzol = 0
        block_polished_andesite = 0
        block_poppy = 0
        block_potatoes = 0
        block_potted_acacia_sapling = 0
        block_potted_birch_sapling = 0
        block_potted_brown_mushroom = 0
        block_potted_cactus = 0
        block_potted_dandelion = 0
        block_potted_dark_oak_sapling = 0
        block_potted_dead_bush = 0
        block_potted_fern = 0
        block_potted_jungle_sapling = 0
        block_potted_oak_sapling = 0
        block_potted_poppy = 0
        block_potted_red_mushroom = 0
        block_potted_spruce_sapling = 0
        block_prismarine = 0
        block_prismarine_bricks = 0
        block_pumpkin_stem = 0
        block_purple_carpet = 0
        block_rail = 0
        block_red_carpet = 0
        block_red_mushroom = 0
        block_red_mushroom_block = 0
        block_red_sand = 0
        block_red_sandstone = 0
        block_red_sandstone_slab = 0
        block_red_sandstone_stairs = 0
        block_red_terracotta = 0
        block_red_tulip = 0
        block_red_wool = 0
        block_redstone_ore = 0
        block_redstone_torch = 0
        block_redstone_wire = 0
        block_repeater = 0
        block_rose_bush = 0
        block_sand = 0
        block_sandstone = 0
        block_sandstone_slab = 0
        block_sandstone_stairs = 0
        block_sea_lantern = 0
        block_smooth_sandstone = 0
        block_smooth_stone = 0
        block_smooth_stone_slab = 0
        block_snow = 0
        block_snow_block = 0
        block_spawner = 0
        block_spruce_door = 0
        block_spruce_fence = 0
        block_spruce_leaves = 0
        block_spruce_log = 0
        block_spruce_planks = 0
        block_spruce_slab = 0
        block_spruce_stairs = 0
        block_stone = 0
        block_stone_brick_slab = 0
        block_stone_brick_stairs = 0
        block_stone_bricks = 0
        block_stone_button = 0
        block_stone_pressure_plate = 0
        block_sugar_cane = 0
        block_sunflower = 0
        block_tall_grass = 0
        block_terracotta = 0
        block_tnt = 0
        block_torch = 0
        block_trapped_chest = 0
        block_tripwire = 0
        block_tripwire_hook = 0
        block_vine = 0
        block_water = 0
        block_wet_sponge = 0
        block_wheat = 0
        block_white_carpet = 0
        block_white_terracotta = 0
        block_white_tulip = 0
        block_white_wool = 0
        block_wooden_slab = 0
        block_yellow_carpet = 0
        block_yellow_terracotta = 0
        block_yellow_wool = 0

        region_path = concatenate_paths(path_to_regions, region_file_name)
        Region = anvil.region.Region(read_file(region_path, 'rb'))

        for (ch_x, ch_z) in get_all_chunk_coords_from_region(region_path):
            Chunk = Region.get_chunk(ch_x, ch_z)

            for b_y in CHUNK_HEIGHT_RANGE:
                for b_x in CHUNK_WIDTH_RANGE:
                    for b_z in CHUNK_LENGTH_RANGE:

                        b = Chunk.get_block(b_x, b_y, b_z)

                        b_id = b.id
                        b_data = b.data

                        if b_id == 0:
                            block_air += 1
                        
                        elif b_id == 1:
                            if b_data == 0:
                                block_stone += 1
                            elif b_data == 1:
                                block_granite += 1
                            elif b_data == 3:
                                block_diorite += 1
                            elif b_data == 5:
                                block_andesite += 1
                            elif b_data == 6:
                                block_polished_andesite += 1
                            else:
                                log_error(f'Invalid b_data: {b_id=}; {b_data=}')
                                exit()

                        elif b_id == 2:
                            block_grass_block += 1

                        elif b_id == 3:
                            if b_data == 0:
                                block_dirt += 1
                            elif b_data == 1:
                                block_coarse_dirt += 1
                            elif b_data == 2:
                                block_podzol += 1

                        elif b_id == 4:
                            block_cobblestone += 1

                        elif b_id == 5:
                            if b_data == 0:
                                block_oak_planks += 1
                            elif b_data == 1:
                                block_spruce_planks += 1
                            elif b_data == 2:
                                block_birch_planks += 1
                            elif b_data == 4:
                                block_acacia_planks += 1
                            elif b_data == 5:
                                block_dark_oak_planks += 1
                            else:
                                log_error(f'Invalid b_data: {b_id=}; {b_data=}')
                                exit()

                        elif b_id == 7:
                            block_bedrock += 1

                        elif b_id == 8:
                            block_water += 1

                        elif b_id == 9:
                            block_water += 1

                        elif b_id == 10:
                            block_lava += 1

                        elif b_id == 11:
                            block_lava += 1

                        elif b_id == 12:
                            if b_data == 0:
                                block_sand += 1
                            elif b_data == 1:
                                block_red_sand += 1

                        elif b_id == 13:
                            block_gravel += 1

                        elif b_id == 14:
                            block_gold_ore += 1

                        elif b_id == 15:
                            block_iron_ore += 1

                        elif b_id == 16:
                            block_coal_ore += 1

                        elif b_id == 17:
                            if b_data == 0:
                                block_oak_log += 1
                            elif b_data == 1:
                                block_spruce_log += 1
                            elif b_data == 2:
                                block_birch_log += 1
                            elif b_data == 3:
                                block_jungle_log += 1
                            elif b_data == 4:
                                block_oak_log += 1
                            elif b_data == 5:
                                block_spruce_log += 1
                            elif b_data == 6:
                                block_birch_log += 1
                            elif b_data == 7:
                                block_jungle_log += 1
                            elif b_data == 8:
                                block_oak_log += 1
                            elif b_data == 9:
                                block_spruce_log += 1
                            elif b_data == 10:
                                block_birch_log += 1
                            elif b_data == 11:
                                block_jungle_log += 1
                            elif b_data == 12:
                                block_oak_log += 1
                            elif b_data == 13:
                                block_spruce_log += 1
                            elif b_data == 14:
                                block_birch_log += 1
                            elif b_data == 15:
                                block_jungle_log += 1

                        elif b_id == 18:
                            if b_data == 0:
                                block_oak_leaves += 1
                            elif b_data == 1:
                                block_spruce_leaves += 1
                            elif b_data == 2:
                                block_birch_leaves += 1
                            elif b_data == 3:
                                block_jungle_leaves += 1
                            elif b_data == 4:
                                block_oak_leaves += 1
                            elif b_data == 5:
                                block_spruce_leaves += 1
                            elif b_data == 6:
                                block_birch_leaves += 1
                            elif b_data == 7:
                                block_jungle_leaves += 1
                            elif b_data == 8:
                                block_oak_leaves += 1
                            elif b_data == 9:
                                block_spruce_leaves += 1
                            elif b_data == 10:
                                block_birch_leaves += 1
                            elif b_data == 11:
                                block_jungle_leaves += 1
                            elif b_data == 12:
                                block_oak_leaves += 1
                            elif b_data == 13:
                                block_spruce_leaves += 1
                            elif b_data == 14:
                                block_birch_leaves += 1
                            elif b_data == 15:
                                block_jungle_leaves += 1

                        elif b_id == 19:
                            if b_data == 1:
                                block_wet_sponge += 1
                            else:
                                log_error(f'Invalid b_data: {b_id=}; {b_data=}')
                                exit()

                        elif b_id == 20:
                            block_glass += 1

                        elif b_id == 21:
                            block_lapis_ore += 1

                        elif b_id == 22:
                            block_lapis_block += 1

                        elif b_id == 23:
                            block_dispenser += 1

                        elif b_id == 24:
                            if b_data == 0:
                                block_sandstone += 1
                            elif b_data == 1:
                                block_chiseled_sandstone += 1
                            elif b_data == 2:
                                block_cut_sandstone += 1
                            else:
                                log_error(f'Invalid b_data: {b_id=}; {b_data=}')
                                exit()

                        elif b_id == 26:
                            block_bed += 1

                        elif b_id == 27:
                            block_powered_rail += 1

                        elif b_id == 29:
                            block_sticky_piston += 1

                        elif b_id == 30:
                            block_cobweb += 1

                        elif b_id == 31:
                            if b_data == 0:
                                block_dead_shrub += 1
                            elif b_data == 1:
                                block_grass += 1
                            elif b_data == 2:
                                block_fern += 1

                        elif b_id == 32:
                            block_dead_bush += 1

                        elif b_id == 35:
                            if b_data == 0:
                                block_white_wool += 1
                            elif b_data == 1:
                                block_orange_wool += 1
                            elif b_data == 3:
                                block_light_blue_wool += 1
                            elif b_data == 4:
                                block_yellow_wool += 1
                            elif b_data == 5:
                                block_lime_wool += 1
                            elif b_data == 7:
                                block_gray_wool += 1
                            elif b_data == 8:
                                block_light_gray_wool += 1
                            elif b_data == 9:
                                block_cyan_wool += 1
                            elif b_data == 11:
                                block_blue_wool += 1
                            elif b_data == 12:
                                block_brown_wool += 1
                            elif b_data == 13:
                                block_green_wool += 1
                            elif b_data == 14:
                                block_red_wool += 1
                            elif b_data == 15:
                                block_black_wool += 1
                            else:
                                log_error(f'Invalid b_data: {b_id=}; {b_data=}')
                                exit()

                        elif b_id == 37:
                            block_dandelion += 1

                        elif b_id == 38:
                            if b_data == 0:
                                block_poppy += 1
                            elif b_data == 1:
                                block_blue_orchid += 1
                            elif b_data == 2:
                                block_allium += 1
                            elif b_data == 3:
                                block_azure_bluet += 1
                            elif b_data == 4:
                                block_red_tulip += 1
                            elif b_data == 5:
                                block_orange_tulip += 1
                            elif b_data == 6:
                                block_white_tulip += 1
                            elif b_data == 7:
                                block_pink_tulip += 1
                            elif b_data == 8:
                                block_oxeye_daise += 1

                        elif b_id == 39:
                            block_brown_mushroom += 1
                        
                        elif b_id == 40:
                            block_red_mushroom += 1

                        elif b_id == 41:
                            block_gold_block += 1

                        elif b_id == 42:
                            block_iron_block += 1

                        elif b_id == 43:
                            if b_data == 0:
                                block_smooth_stone_slab += 1
                            elif b_data == 1:
                                block_sandstone_slab += 1
                            elif b_data == 2:
                                block_petrified_oak_slab += 1
                            elif b_data == 3:
                                block_cobblestone_slab += 1
                            elif b_data == 4:
                                block_brick_slab += 1
                            elif b_data == 6:
                                block_nether_brick_slab += 1
                            elif b_data == 7:
                                block_quartz_slab += 1
                            elif b_data == 8:
                                block_smooth_stone += 1
                            elif b_data == 9:
                                block_smooth_sandstone += 1
                            elif b_data == 11:
                                block_cobblestone_slab += 1
                            elif b_data == 12:
                                block_brick_slab += 1
                            elif b_data == 14:
                                block_nether_brick_slab += 1
                            elif b_data == 15:
                                block_smooth_quartz += 1
                            else:
                                log_error(f'Invalid b_data: {b_id=}; {b_data=}')
                                exit()

                        elif b_id == 44:
                            if b_data == 0:
                                block_smooth_stone_slab += 1
                            elif b_data == 1:
                                block_sandstone_slab += 1
                            elif b_data == 2:
                                block_wooden_slab += 1
                            elif b_data == 3:
                                block_cobblestone_slab += 1
                            elif b_data == 5:
                                block_stone_brick_slab += 1
                            elif b_data == 8:
                                block_smooth_stone_slab += 1
                            elif b_data == 9:
                                block_sandstone_slab += 1
                            elif b_data == 10:
                                block_wooden_slab += 1
                            elif b_data == 11:
                                block_cobblestone_slab += 1
                            else:
                                log_error(f'Invalid b_data: {b_id=}; {b_data=}')
                                exit()

                        elif b_id == 46:
                            block_tnt += 1

                        elif b_id == 47:
                            block_bookshelf += 1

                        elif b_id == 48:
                            block_mossy_cobblestone += 1

                        elif b_id == 49:
                            block_obsidian += 1

                        elif b_id == 50:
                            block_torch += 1

                        elif b_id == 52:
                            block_spawner += 1

                        elif b_id == 53:
                            block_oak_stairs += 1

                        elif b_id == 54:
                            block_chest += 1

                        elif b_id == 55:
                            block_redstone_wire += 1

                        elif b_id == 56:
                            block_diamond_ore += 1

                        elif b_id == 57:
                            block_diamond_block += 1

                        elif b_id == 58:
                            block_crafting_table += 1

                        elif b_id == 59:
                            block_wheat += 1

                        elif b_id == 60:
                            block_farmland += 1

                        elif b_id == 61:
                            block_furnace += 1

                        elif b_id == 62:
                            block_furnace += 1

                        elif b_id == 63:
                            block_oak_sign += 1

                        elif b_id == 64:
                            block_oak_door += 1

                        elif b_id == 65:
                            block_ladder += 1

                        elif b_id == 66:
                            block_rail += 1

                        elif b_id == 67:
                            block_cobblestone_stairs += 1

                        elif b_id == 68: # Oak wall sign <=> oak sign
                            block_oak_sign += 1

                        elif b_id == 69:
                            block_lever += 1

                        elif b_id == 70:
                            block_stone_pressure_plate += 1

                        elif b_id == 71:
                            block_iron_door += 1

                        elif b_id == 72:
                            block_oak_pressure_plate += 1

                        elif b_id == 73:
                            block_redstone_ore += 1

                        elif b_id == 74:
                            block_redstone_ore += 1

                        elif b_id == 75: # Redstone wall torch <=> redstone torch
                            block_redstone_torch += 1

                        elif b_id == 76:
                            block_redstone_torch += 1

                        elif b_id == 77:
                            block_stone_button += 1

                        elif b_id == 78:
                            block_snow += 1

                        elif b_id == 79:
                            block_ice += 1

                        elif b_id == 80:
                            block_snow_block += 1

                        elif b_id == 81:
                            block_cactus += 1

                        elif b_id == 82:
                            block_clay += 1

                        elif b_id == 83:
                            block_sugar_cane += 1

                        elif b_id == 84:
                            block_jukebox += 1

                        elif b_id == 85:
                            block_oak_fence += 1

                        elif b_id == 86:
                            block_carved_pumpkin += 1

                        elif b_id == 93:
                            block_repeater += 1

                        elif b_id == 94:
                            block_repeater += 1

                        elif b_id == 96:
                            block_oak_trapdoor += 1

                        elif b_id == 97:
                            if b_data == 0:
                                block_infested_stone += 1
                            elif b_data == 1:
                                block_infested_cobblestone += 1
                            elif b_data == 2:
                                block_infested_stone_bricks += 1
                            elif b_data == 3:
                                block_infested_mossy_stone_bricks += 1
                            elif b_data == 4:
                                block_infested_cracked_stone_bricks += 1
                            elif b_data == 5:
                                block_infested_chiseled_stone_bricks += 1

                        elif b_id == 98:
                            if b_data == 0:
                                block_stone_bricks += 1
                            elif b_data == 1:
                                block_mossy_stone_bricks += 1
                            elif b_data == 2:
                                block_cracked_stone_bricks += 1
                            elif b_data == 3:
                                block_chiseled_stone_bricks += 1
                            #else:
                            #    log_error(f'Invalid b_data: {b_id=}; {b_data=}')
                            #    exit()

                        elif b_id == 99:
                            block_brown_mushroom_block += 1

                        elif b_id == 100:
                            block_red_mushroom_block += 1

                        elif b_id == 101:
                            block_iron_bars += 1

                        elif b_id == 102:
                            block_glass_pane += 1

                        elif b_id == 103:
                            block_melon += 1

                        elif b_id == 106:
                            block_vine += 1

                        elif b_id == 109:
                            block_stone_brick_stairs += 1

                        elif b_id == 110:
                            block_mycelium += 1

                        elif b_id == 111:
                            block_lily_pad += 1

                        elif b_id == 117:
                            block_brewing_stand += 1

                        elif b_id == 118:
                            block_cauldron += 1

                        elif b_id == 120:
                            block_end_portal_frame += 1

                        elif b_id == 125:
                            if b_data == 0:
                                block_oak_slab += 1
                            elif b_data == 1:
                                block_spruce_slab += 1
                            elif b_data == 2:
                                block_birch_slab += 1
                            else:
                                log_error(f'Invalid b_data: {b_id=}; {b_data=}')
                                exit()

                        elif b_id == 126:
                            if b_data == 9:
                                block_spruce_slab += 1
                            else:
                                log_error(f'Invalid b_data: {b_id=}; {b_data=}')
                                exit()

                        elif b_id == 127:
                            block_cocoa += 1

                        elif b_id == 128:
                            block_sandstone_stairs += 1

                        elif b_id == 129:
                            block_emerald_ore += 1

                        elif b_id == 131:
                            block_tripwire_hook += 1

                        elif b_id == 132:
                            block_tripwire += 1

                        elif b_id == 134:
                            block_spruce_stairs += 1

                        elif b_id == 135:
                            block_birch_stairs += 1

                        elif b_id == 139:
                            if b_data == 0:
                                block_cobblestone_wall += 1
                            elif b_data == 1:
                                block_mossy_cobblestone_wall += 1

                        elif b_id == 140:
                            if b_data == 0:
                                block_flower_pot += 1
                            elif b_data == 1:
                                block_potted_poppy += 1
                            elif b_data == 2:
                                block_potted_dandelion += 1
                            elif b_data == 3:
                                block_potted_oak_sapling += 1
                            elif b_data == 4:
                                block_potted_spruce_sapling += 1
                            elif b_data == 5:
                                block_potted_birch_sapling += 1
                            elif b_data == 6:
                                block_potted_jungle_sapling += 1
                            elif b_data == 7:
                                block_potted_red_mushroom += 1
                            elif b_data == 8:
                                block_potted_brown_mushroom += 1
                            elif b_data == 9:
                                block_potted_cactus += 1
                            elif b_data == 10:
                                block_potted_dead_bush += 1
                            elif b_data == 11:
                                block_potted_fern += 1
                            elif b_data == 12:
                                block_potted_acacia_sapling += 1
                            elif b_data == 13:
                                block_potted_dark_oak_sapling += 1
                            elif b_data == 14:
                                block_flower_pot += 1
                            elif b_data == 15:
                                block_flower_pot += 1

                        elif b_id == 141:
                            block_carrots += 1

                        elif b_id == 142:
                            block_potatoes += 1

                        elif b_id == 146:
                            block_trapped_chest += 1

                        elif b_id == 159:
                            if b_data == 0:
                                block_white_terracotta += 1
                            elif b_data == 1:
                                block_orange_terracotta += 1
                            elif b_data == 4:
                                block_yellow_terracotta += 1
                            elif b_data == 8:
                                block_light_gray_terracotta += 1
                            elif b_data == 11:
                                block_blue_terracotta += 1
                            elif b_data == 12:
                                block_brown_terracotta += 1
                            elif b_data == 14:
                                block_red_terracotta += 1
                            else:
                                log_error(f'Invalid b_data: {b_id=}; {b_data=}')
                                exit()

                        elif b_id == 161:
                            if b_data == 0:
                                block_acacia_leaves += 1
                            elif b_data == 1:
                                block_dark_oak_leaves += 1
                            elif b_data == 4:
                                block_acacia_leaves += 1
                            elif b_data == 5:
                                block_dark_oak_leaves += 1
                            elif b_data == 8:
                                block_acacia_leaves += 1
                            elif b_data == 9:
                                block_dark_oak_leaves += 1
                            elif b_data == 12:
                                block_acacia_leaves += 1
                            elif b_data == 13:
                                block_dark_oak_leaves += 1

                        elif b_id == 162:
                            if b_data == 0:
                                block_acacia_log += 1
                            elif b_data == 1:
                                block_dark_oak_log += 1
                            elif b_data == 4:
                                block_acacia_log += 1
                            elif b_data == 5:
                                block_dark_oak_log += 1
                            elif b_data == 8:
                                block_acacia_log += 1
                            elif b_data == 9:
                                block_dark_oak_log += 1
                            elif b_data == 12:
                                block_acacia_log += 1
                            elif b_data == 13:
                                block_dark_oak_log += 1

                        elif b_id == 163:
                            block_acacia_stairs += 1

                        elif b_id == 164:
                            block_dark_oak_stairs += 1

                        elif b_id == 168:
                            if b_data == 0:
                                block_prismarine += 1
                            elif b_data == 1:
                                block_prismarine_bricks += 1
                            elif b_data == 2:
                                block_dark_prismarine += 1

                        elif b_id == 169:
                            block_sea_lantern += 1

                        elif b_id == 171:
                            if b_data == 0:
                                block_white_carpet += 1
                            elif b_data == 1:
                                block_orange_carpet += 1
                            elif b_data == 2:
                                block_magenta_carpet += 1
                            elif b_data == 3:
                                block_light_blue_carpet += 1
                            elif b_data == 4:
                                block_yellow_carpet += 1
                            elif b_data == 5:
                                block_lime_carpet += 1
                            elif b_data == 6:
                                block_pink_carpet += 1
                            elif b_data == 7:
                                block_gray_carpet += 1
                            elif b_data == 8:
                                block_light_gray_carpet += 1
                            elif b_data == 9:
                                block_cyan_carpet += 1
                            elif b_data == 10:
                                block_purple_carpet += 1
                            elif b_data == 11:
                                block_blue_carpet += 1
                            elif b_data == 12:
                                block_brown_carpet += 1
                            elif b_data == 13:
                                block_green_carpet += 1
                            elif b_data == 14:
                                block_red_carpet += 1
                            elif b_data == 15:
                                block_black_carpet += 1

                        elif b_id == 172:
                            block_terracotta += 1

                        elif b_id == 174:
                            block_packed_ice += 1

                        elif b_id == 175:
                            if b_data == 0:
                                block_sunflower += 1
                            elif b_data == 1:
                                block_lilac += 1
                            elif b_data == 2:
                                block_tall_grass += 1
                            elif b_data == 3:
                                block_large_fern += 1
                            elif b_data == 4:
                                block_rose_bush += 1
                            elif b_data == 5:
                                block_peony += 1
                            elif b_data == 8:
                                block_sunflower += 1
                            elif b_data == 9:
                                block_lilac += 1
                            elif b_data == 10:
                                block_tall_grass += 1
                            elif b_data == 11:
                                block_large_fern += 1
                            elif b_data == 12:
                                block_rose_bush += 1
                            elif b_data == 13:
                                block_peony += 1

                        elif b_id == 179:
                            if b_data == 0:
                                block_red_sandstone += 1
                            else:
                                log_error(f'Invalid b_data: {b_id=}; {b_data=}')

                        elif b_id == 180:
                            block_red_sandstone_stairs += 1

                        elif b_id == 181:
                            if b_data == 0:
                                block_red_sandstone += 1
                            elif b_data == 2:
                                block_prismarine += 1
                            elif b_data == 3:
                                block_prismarine_bricks += 1
                            elif b_data == 4:
                                block_dark_prismarine += 1

                        elif b_id == 182:
                            block_red_sandstone_slab += 1

                        elif b_id == 186:
                            block_dark_oak_fence_gate += 1
                        
                        elif b_id == 188:
                            block_spruce_fence += 1

                        elif b_id == 189:
                            block_birch_fence += 1

                        elif b_id == 191:
                            block_dark_oak_fence += 1

                        elif b_id == 192:
                            block_acacia_fence += 1

                        elif b_id == 193:
                            block_spruce_door += 1

                        elif b_id == 196:
                            block_acacia_door += 1

                        elif b_id == 207:
                            block_beetroots += 1

                        elif b_id == 208:
                            block_grass_path += 1

                        elif b_id == 216:
                            block_bone_block += 1

                        else:
                            log_error(f'Invalid block: {b_id=}; {b_data=}\n')
                            exit()

            log_info(f'Chunk at {ch_x}; {ch_z} finished!', end='')

        with open(concatenate_paths(OUTPUT_FOLDER, region_file_name), 'w') as f:
            f.write(f'{block_acacia_door=}\n')
            f.write(f'{block_acacia_fence=}\n')
            f.write(f'{block_acacia_leaves=}\n')
            f.write(f'{block_acacia_log=}\n')
            f.write(f'{block_acacia_planks=}\n')
            f.write(f'{block_acacia_stairs=}\n')
            f.write(f'{block_air=}\n')
            f.write(f'{block_allium=}\n')
            f.write(f'{block_andesite=}\n')
            f.write(f'{block_azure_bluet=}\n')
            f.write(f'{block_bed=}\n')
            f.write(f'{block_bedrock=}\n')
            f.write(f'{block_beetroots=}\n')
            f.write(f'{block_birch_fence=}\n')
            f.write(f'{block_birch_leaves=}\n')
            f.write(f'{block_birch_log=}\n')
            f.write(f'{block_birch_planks=}\n')
            f.write(f'{block_birch_slab=}\n')
            f.write(f'{block_birch_stairs=}\n')
            f.write(f'{block_black_carpet=}\n')
            f.write(f'{block_black_wool=}\n')
            f.write(f'{block_blue_carpet=}\n')
            f.write(f'{block_blue_orchid=}\n')
            f.write(f'{block_blue_terracotta=}\n')
            f.write(f'{block_blue_wool=}\n')
            f.write(f'{block_bone_block=}\n')
            f.write(f'{block_bookshelf=}\n')
            f.write(f'{block_brewing_stand=}\n')
            f.write(f'{block_brown_carpet=}\n')
            f.write(f'{block_brown_mushroom=}\n')
            f.write(f'{block_brown_mushroom_block=}\n')
            f.write(f'{block_brown_terracotta=}\n')
            f.write(f'{block_brown_wool=}\n')
            f.write(f'{block_cactus=}\n')
            f.write(f'{block_carrots=}\n')
            f.write(f'{block_carved_pumpkin=}\n')
            f.write(f'{block_cauldron=}\n')
            f.write(f'{block_chest=}\n')
            f.write(f'{block_chiseled_sandstone=}\n')
            f.write(f'{block_chiseled_stone_bricks=}\n')
            f.write(f'{block_clay=}\n')
            f.write(f'{block_coal_ore=}\n')
            f.write(f'{block_coarse_dirt=}\n')
            f.write(f'{block_cobblestone=}\n')
            f.write(f'{block_cobblestone_slab=}\n')
            f.write(f'{block_cobblestone_stairs=}\n')
            f.write(f'{block_cobblestone_wall=}\n')
            f.write(f'{block_cobweb=}\n')
            f.write(f'{block_cocoa=}\n')
            f.write(f'{block_cracked_stone_bricks=}\n')
            f.write(f'{block_crafting_table=}\n')
            f.write(f'{block_cut_sandstone=}\n')
            f.write(f'{block_cyan_carpet=}\n')
            f.write(f'{block_cyan_wool=}\n')
            f.write(f'{block_dandelion=}\n')
            f.write(f'{block_dark_oak_fence=}\n')
            f.write(f'{block_dark_oak_fence_gate=}\n')
            f.write(f'{block_dark_oak_leaves=}\n')
            f.write(f'{block_dark_oak_log=}\n')
            f.write(f'{block_dark_oak_planks=}\n')
            f.write(f'{block_dark_oak_sapling=}\n')
            f.write(f'{block_dark_oak_stairs=}\n')
            f.write(f'{block_dark_prismarine=}\n')
            f.write(f'{block_dead_bush=}\n')
            f.write(f'{block_dead_shrub=}\n')
            f.write(f'{block_diamond_block=}\n')
            f.write(f'{block_diamond_ore=}\n')
            f.write(f'{block_diorite=}\n')
            f.write(f'{block_dirt=}\n')
            f.write(f'{block_dispenser=}\n')
            f.write(f'{block_emerald_ore=}\n')
            f.write(f'{block_end_portal_frame=}\n')
            f.write(f'{block_farmland=}\n')
            f.write(f'{block_fern=}\n')
            f.write(f'{block_flower_pot=}\n')
            f.write(f'{block_furnace=}\n')
            f.write(f'{block_glass=}\n')
            f.write(f'{block_glass_pane=}\n')
            f.write(f'{block_gold_ore=}\n')
            f.write(f'{block_granite=}\n')
            f.write(f'{block_grass=}\n')
            f.write(f'{block_grass_block=}\n')
            f.write(f'{block_grass_path=}\n')
            f.write(f'{block_gravel=}\n')
            f.write(f'{block_gray_carpet=}\n')
            f.write(f'{block_gray_wool=}\n')
            f.write(f'{block_green_carpet=}\n')
            f.write(f'{block_green_wool=}\n')
            f.write(f'{block_ice=}\n')
            f.write(f'{block_infested_chiseled_stone_bricks=}\n')
            f.write(f'{block_infested_cobblestone=}\n')
            f.write(f'{block_infested_cracked_stone_bricks=}\n')
            f.write(f'{block_infested_mossy_stone_bricks=}\n')
            f.write(f'{block_infested_stone=}\n')
            f.write(f'{block_infested_stone_bricks=}\n')
            f.write(f'{block_iron_bars=}\n')
            f.write(f'{block_iron_door=}\n')
            f.write(f'{block_iron_ore=}\n')
            f.write(f'{block_jungle_leaves=}\n')
            f.write(f'{block_jungle_log=}\n')
            f.write(f'{block_ladder=}\n')
            f.write(f'{block_lapis_block=}\n')
            f.write(f'{block_lapis_ore=}\n')
            f.write(f'{block_large_fern=}\n')
            f.write(f'{block_lava=}\n')
            f.write(f'{block_lever=}\n')
            f.write(f'{block_light_blue_carpet=}\n')
            f.write(f'{block_light_blue_wool=}\n')
            f.write(f'{block_light_gray_carpet=}\n')
            f.write(f'{block_light_gray_terracotta=}\n')
            f.write(f'{block_light_gray_wool=}\n')
            f.write(f'{block_lilac=}\n')
            f.write(f'{block_lily_pad=}\n')
            f.write(f'{block_lime_carpet=}\n')
            f.write(f'{block_lime_wool=}\n')
            f.write(f'{block_magenta_carpet=}\n')
            f.write(f'{block_melon=}\n')
            f.write(f'{block_melon_stem=}\n')
            f.write(f'{block_mossy_cobblestone=}\n')
            f.write(f'{block_mossy_cobblestone_wall=}\n')
            f.write(f'{block_mossy_stone_bricks=}\n')
            f.write(f'{block_mycelium=}\n')
            f.write(f'{block_oak_door=}\n')
            f.write(f'{block_oak_fence=}\n')
            f.write(f'{block_oak_leaves=}\n')
            f.write(f'{block_oak_log=}\n')
            f.write(f'{block_oak_planks=}\n')
            f.write(f'{block_oak_pressure_plate=}\n')
            f.write(f'{block_oak_sign=}\n')
            f.write(f'{block_oak_slab=}\n')
            f.write(f'{block_oak_stairs=}\n')
            f.write(f'{block_oak_trapdoor=}\n')
            f.write(f'{block_obsidian=}\n')
            f.write(f'{block_orange_carpet=}\n')
            f.write(f'{block_orange_terracotta=}\n')
            f.write(f'{block_orange_tulip=}\n')
            f.write(f'{block_orange_wool=}\n')
            f.write(f'{block_oxeye_daise=}\n')
            f.write(f'{block_packed_ice=}\n')
            f.write(f'{block_peony=}\n')
            f.write(f'{block_pink_carpet=}\n')
            f.write(f'{block_pink_tulip=}\n')
            f.write(f'{block_podzol=}\n')
            f.write(f'{block_polished_andesite=}\n')
            f.write(f'{block_poppy=}\n')
            f.write(f'{block_potatoes=}\n')
            f.write(f'{block_potted_acacia_sapling=}\n')
            f.write(f'{block_potted_birch_sapling=}\n')
            f.write(f'{block_potted_brown_mushroom=}\n')
            f.write(f'{block_potted_cactus=}\n')
            f.write(f'{block_potted_dandelion=}\n')
            f.write(f'{block_potted_dark_oak_sapling=}\n')
            f.write(f'{block_potted_dead_bush=}\n')
            f.write(f'{block_potted_fern=}\n')
            f.write(f'{block_potted_jungle_sapling=}\n')
            f.write(f'{block_potted_oak_sapling=}\n')
            f.write(f'{block_potted_poppy=}\n')
            f.write(f'{block_potted_red_mushroom=}\n')
            f.write(f'{block_potted_spruce_sapling=}\n')
            f.write(f'{block_prismarine=}\n')
            f.write(f'{block_prismarine_bricks=}\n')
            f.write(f'{block_pumpkin_stem=}\n')
            f.write(f'{block_purple_carpet=}\n')
            f.write(f'{block_rail=}\n')
            f.write(f'{block_red_carpet=}\n')
            f.write(f'{block_red_mushroom=}\n')
            f.write(f'{block_red_mushroom_block=}\n')
            f.write(f'{block_red_sand=}\n')
            f.write(f'{block_red_sandstone=}\n')
            f.write(f'{block_red_sandstone_slab=}\n')
            f.write(f'{block_red_sandstone_stairs=}\n')
            f.write(f'{block_red_terracotta=}\n')
            f.write(f'{block_red_tulip=}\n')
            f.write(f'{block_red_wool=}\n')
            f.write(f'{block_redstone_ore=}\n')
            f.write(f'{block_redstone_torch=}\n')
            f.write(f'{block_redstone_wire=}\n')
            f.write(f'{block_repeater=}\n')
            f.write(f'{block_rose_bush=}\n')
            f.write(f'{block_sand=}\n')
            f.write(f'{block_sandstone=}\n')
            f.write(f'{block_sandstone_slab=}\n')
            f.write(f'{block_sandstone_stairs=}\n')
            f.write(f'{block_sea_lantern=}\n')
            f.write(f'{block_smooth_sandstone=}\n')
            f.write(f'{block_smooth_stone=}\n')
            f.write(f'{block_smooth_stone_slab=}\n')
            f.write(f'{block_snow=}\n')
            f.write(f'{block_snow_block=}\n')
            f.write(f'{block_spawner=}\n')
            f.write(f'{block_spruce_door=}\n')
            f.write(f'{block_spruce_fence=}\n')
            f.write(f'{block_spruce_leaves=}\n')
            f.write(f'{block_spruce_log=}\n')
            f.write(f'{block_spruce_planks=}\n')
            f.write(f'{block_spruce_slab=}\n')
            f.write(f'{block_spruce_stairs=}\n')
            f.write(f'{block_stone=}\n')
            f.write(f'{block_stone_brick_slab=}\n')
            f.write(f'{block_stone_brick_stairs=}\n')
            f.write(f'{block_stone_bricks=}\n')
            f.write(f'{block_stone_button=}\n')
            f.write(f'{block_stone_pressure_plate=}\n')
            f.write(f'{block_sugar_cane=}\n')
            f.write(f'{block_sunflower=}\n')
            f.write(f'{block_tall_grass=}\n')
            f.write(f'{block_terracotta=}\n')
            f.write(f'{block_tnt=}\n')
            f.write(f'{block_torch=}\n')
            f.write(f'{block_trapped_chest=}\n')
            f.write(f'{block_tripwire=}\n')
            f.write(f'{block_tripwire_hook=}\n')
            f.write(f'{block_vine=}\n')
            f.write(f'{block_water=}\n')
            f.write(f'{block_wet_sponge=}\n')
            f.write(f'{block_wheat=}\n')
            f.write(f'{block_white_carpet=}\n')
            f.write(f'{block_white_terracotta=}\n')
            f.write(f'{block_white_tulip=}\n')
            f.write(f'{block_white_wool=}\n')
            f.write(f'{block_wooden_slab=}\n')
            f.write(f'{block_yellow_carpet=}\n')
            f.write(f'{block_yellow_terracotta=}\n')
            f.write(f'{block_yellow_wool=}')

        log_info('Save used region files!     \n')
        used_region_file_names.append(region_file_name)
        with open(OUTPUT_USED_REGION_FILE_NAMES, 'w') as f:
            f.write('\n'.join(used_region_file_names))

    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is description.')
    parser.add_argument(
        '-o', '--output', default='result', type=str, help='Output folder for result.',
        required=False
    )
    parser.add_argument(
        '-i', '--input', type=str, help='Input folder for minecraft world aka "saves/my_world".',
        required=True
    )
    args = parser.parse_args()
    main(args)

