import serverCommunication
import gameGenerator
import json

if __name__ == '__main__':
    token = serverCommunication.login()
    # serverCommunication.game_train(token,"test1.txt",1,8)

    game_state_json2 = open('game_state.json')

    gameGenerator.create_hexagon_game_map(game_state_json2.read())
    #serverCommunication.join_game(token)
    #serverCommunication.game_do_action(token,"move","-6","-7")
    # serverCommunication.game_action_train(token, "move", "-7", "-7")

