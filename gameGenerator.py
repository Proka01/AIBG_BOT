import json


def get_my_player_id(game_state_json):
    game_state_data = json.loads(game_state_json)

    return game_state_data['playerIdx']


def create_player_info(game_state_json):
    players_map = {}
    game_state_data = json.loads(game_state_json)
    game_state = game_state_data['gameState']
    #print("stateeee ", json.loads(game_state)['player1'])

    game_players = json.loads(game_state)
    for i in range(1, 5):
        player = game_players[f'player{i}']
        players_map[player['playerIdx']] = player
        #player = players[f'player{i}']
        #players_map[player['playerIdx']] = player

    return players_map


def create_hexagon_game_map(game_state_json):
    game_state_data = json.loads(game_state_json)
    game_state = json.loads(game_state_data['gameState'])
    # mapa = json.loads(game_state['map'])
    tiles_arr = game_state['map']['tiles']

    # tiles_arr = game_state_data['gameState']['map']['tiles']

    game_hex_map = {}
    wormhole_map = {}

    for tiles in tiles_arr:
        for tile in tiles:
            q = tile['q']
            r = tile['r']
            entity = tile['entity']

            key = f"{q}:{r}"
            val = entity

            game_hex_map[key] = val

            if entity['type'] == 'WORMHOLE':
                if entity['id'] in wormhole_map.keys():
                    wormhole_map[entity['id']] += [key]
                else:
                    wormhole_map[entity['id']] = [key]

    for dict_key in wormhole_map:
        wormhole_pair = wormhole_map[dict_key]
        key1 = wormhole_pair[0]
        key2 = wormhole_pair[1]

        game_hex_map[key1] = {'type': 'WORMHOLE', 'teleportsTo': f'{key2}'}
        game_hex_map[key2] = {'type': 'WORMHOLE', 'teleportsTo': f'{key1}'}

    # print(game_hex_map)
    # drugi argument je mapa za XP i HP boost, treci argument je niz unutar koga se nalazi mapa sa podacima u formatu {'name': 'neko_ime','power': '50'...}
    return game_hex_map
