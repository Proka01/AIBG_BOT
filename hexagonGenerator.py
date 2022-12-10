import json


def create_hexagon_game_map(game_state_json):
    game_state_data = json.loads(game_state_json)
    tiles_arr = game_state_data['gameState']['map']['tiles']

    game_hex_map = {}

    for tiles in tiles_arr:
        for tile in tiles:
            q = tile['q']
            r = tile['r']
            field_type = tile['entity']

            key = f"{q}:{r}"
            val = field_type

            game_hex_map[key] = val

    print(game_hex_map)
