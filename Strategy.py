import hexagonGenerator as hg

game_state_json = open('game_state.json')
game_map = hg.create_hexagon_game_map(game_state_json.read())
moveq = [0, 1, -1, 1, -1, 0]
mover = [-1, -1, 0, 0, 1 ,1]

q = []
game_map.get()