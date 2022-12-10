import heapq
import math


def dijskstra(start_q, start_r, game_hex_map, players_map, my_id):
    move_q = [0, 1, 1, 0, -1, -1]
    move_r = [-1, -1, 0, 1, 1, 0]

    min_heap = []
    dist_map = {}
    heapq.heappush(min_heap, (0, start_q, start_r))

    for tile in game_hex_map.keys():
        dist_map[tile] = 10 ** 9

    dist_map[f'{start_q}:{start_r}'] = 0

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

            if game_hex_map[next_key]['type'] == 'ASTEROID':
                w = math.ceil(350.0 / players_map[my_id]['power']) + 1
            elif game_hex_map[next_key]['type'] == 'BLACKHOLE':
                w = 3
            else:
                w = 1

            if game_hex_map[next_key]['type'] != 'WORMHOLE':
                if dist_map[key] + w < dist_map[next_key]:
                    dist_map[next_key] = dist_map[key] + w
                    heapq.heappush(min_heap, (dist_map[next_key], qq, rr))
            else:
                qq, rr = game_hex_map[next_key]['teleportsTo'].split(':')
                qq = int(qq) + move_q[i]
                rr = int(rr) + move_r[i]
                if dist_map[key] + w < dist_map[f'{qq}:{rr}']:
                    dist_map[f'{qq}:{rr}'] = dist_map[key] + w
                    heapq.heappush(min_heap, (dist_map[f'{qq}:{rr}'], qq, rr))

    print(dist_map)
    return dist_map
