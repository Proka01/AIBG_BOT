import serverCommunication
import gameGenerator
import dijkstra
import json

if __name__ == '__main__':
    # token = serverCommunication.login()
    # serverCommunication.game_train(token,"test1.txt",1,8)

    game_state_json2 = open('game_state_json2.json')
    content = game_state_json2.read()
    players_map = gameGenerator.create_player_info(content)
    game_hex_map = gameGenerator.create_hexagon_game_map(content)
    dist, par = dijkstra.dijskstra(-7, -7, game_hex_map, players_map, 1)
    dijkstra.next_cell(par, -7, -7, 8, 1)


    #serverCommunication.join_game(token)
    #serverCommunication.game_do_action(token,"move","-6","-7")
    # serverCommunication.game_action_train(token, "move", "-7", "-7")

