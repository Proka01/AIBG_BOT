import heapq
import math


def dijskstra(start_q, start_r, game_hex_map, players_map, my_id):
    move_q = [0, 1, 1, 0, -1, -1]
    move_r = [-1, -1, 0, 1, 1, 0]

    ##dodato
    for player_key in players_map.keys():
        game_hex_map[player_key] = players_map[player_key]

    opponent_adj_cells = {}
    for player_key in players_map.keys():
        if my_id != player_key:
            q = players_map[player_key]['q']
            r = players_map[player_key]['r']

            for i in range(-3, 4):
                for j in range(-3, 4):
                    if i == 0 and j == 0:
                        continue

                    qq = q + i
                    rr = r + j


                    zbir = abs(qq + rr)
                    if zbir < 2:
                        power = 3
                    elif zbir < 3:
                        power = 2
                    else:
                        power = 1

                    adj_cell_key = f'{qq}:{rr}'
                    if adj_cell_key in game_hex_map.keys():
                        opponent_adj_cells[adj_cell_key] = power


    # print("mapa sa svim a i plejerima")
    # print(game_hex_map)

    min_heap = []
    dist_map = {}
    parent_map = {}
    heapq.heappush(min_heap, (0, start_q, start_r))

    for tile in game_hex_map.keys():
        dist_map[tile] = 10 ** 9

    dist_map[f'{start_q}:{start_r}'] = 0
    parent_map[f'{start_q}:{start_r}'] = f'{start_q}:{start_r}'

    while min_heap:
        d, q, r = heapq.heappop(min_heap)

        key = f'{q}:{r}'

        if key not in game_hex_map.keys():
            continue

        if d > dist_map[key]:
            continue

        for i in range(0, 6):
            qq = q + move_q[i]
            rr = r + move_r[i]

            next_key = f'{qq}:{rr}'

            if next_key not in game_hex_map.keys():
                continue

            ##dodato
            if game_hex_map[next_key]['type'] == 'PLAYER':
                continue

            if game_hex_map[next_key]['type'] == 'ASTEROID':
                w = math.ceil(350.0 / players_map[my_id]['power']) + 1
            elif game_hex_map[next_key]['type'] == 'BLACKHOLE':
                w = 3
            else:
                w = 1

            ##dodao
            if next_key in opponent_adj_cells.keys():
                w += opponent_adj_cells[next_key]

            if game_hex_map[next_key]['type'] != 'WORMHOLE':
                if dist_map[key] + w < dist_map[next_key]:
                    dist_map[next_key] = dist_map[key] + w
                    parent_map[next_key] = key
                    heapq.heappush(min_heap, (dist_map[next_key], qq, rr))
            else:
                parent_map[next_key] = key
                qq, rr = game_hex_map[next_key]['teleportsTo'].split(':')
                qq = int(qq) + move_q[i]
                rr = int(rr) + move_r[i]
                if dist_map[key] + w < dist_map[f'{qq}:{rr}']:
                    dist_map[f'{qq}:{rr}'] = dist_map[key] + w
                    parent_map[f'{qq}:{rr}'] = next_key
                    heapq.heappush(min_heap, (dist_map[f'{qq}:{rr}'], qq, rr))

    # print(dist_map)
    # print()
    # print(parent_map)
    return dist_map, parent_map


def next_cell(parent_map, start_q, start_r, end_q, end_r):
    start_key = f'{start_q}:{start_r}'
    next_key = f'{end_q}:{end_r}'
    prev_key = ""

    while next_key != start_key:
        prev_key = next_key
        next_key = parent_map[next_key]

    return prev_key

