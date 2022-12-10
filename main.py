import serverCommunication
import Strategy
import gameGenerator
import dijkstra
import json

if __name__ == '__main__':
    # token = serverCommunication.login()
    # serverCommunication.game_train(token,"test1.txt",1,8)

    # game_state_json2 = open('game_state_json2.json')
    # content = game_state_json2.read()
    # players_map = gameGenerator.create_player_info(content)
    # game_hex_map = gameGenerator.create_hexagon_game_map(content)
    # dist, par = dijkstra.dijskstra(-7, -7, game_hex_map, players_map, 1)
    # dijkstra.next_cell(par, -7, -7, 8, 1)


#################################################### TEST #########################################
    token = serverCommunication.login()
    join_response = serverCommunication.join_game(token)
    my_idx = json.loads(join_response)['playerIdx']
    state = json.loads(join_response)['gameState']

    # game_hex_map = gameGenerator.create_hexagon_game_map(state)
    # all_players = gameGenerator.create_player_info(state)
    # action = Strategy.game_next_move(all_players[1], all_players, game_hex_map)

    while 1:
        all_players = gameGenerator.create_player_info(state)
        game_hex_map = gameGenerator.create_hexagon_game_map(state)
        action = Strategy.game_next_move(all_players[1], all_players, game_hex_map) ## , my_idx)

        state = serverCommunication.game_do_action(token, action[0], action[1], action[2])


    # token = serverCommunication.login()
    # serverCommunication.game_train(token, "test1.txt", 1, 1.5)
    #
    # state = serverCommunication.game_action_train(token, "move", -7, -6)
    # game_hex_map = gameGenerator.create_hexagon_game_map(state)
    # all_players = gameGenerator.create_player_info(state)
    # action = Strategy.game_next_move(all_players[1], all_players, game_hex_map)
    #
    # while 1:
    #     all_players = gameGenerator.create_player_info(state)
    #     game_hex_map = gameGenerator.create_hexagon_game_map(state)
    #     action = Strategy.game_next_move(all_players[1], all_players, game_hex_map)
    #     print(action)
    #     state = serverCommunication.game_action_train(token, action[0], action[1], action[2])

    # while 1:
    #     me = gameGenerator.create_player_info(state)
    #     print(me[1])
        # x = Strategy.game_next_move(me[1])
        # print(x)
        #state = serverCommunication.game_action_train(token, )

    #serverCommunication.join_game(token)
    #serverCommunication.game_do_action(token,"move","-6","-7")
    # serverCommunication.game_action_train(token, "move", "-7", "-7")

