import serverCommunication
import hexagonGenerator
import json

if __name__ == '__main__':
    #token = serverCommunication.login()
    #serverCommunication.game_train(token,"test1.txt",1,8)

    game_state_json = open('game_state.json')

    hexagonGenerator.create_hexagon_game_map(game_state_json.read())
    #serverCommunication.join_game(token)
    #serverCommunication.game_do_action(token,"move","-6","-7")
    #serverCommunication.game_action_train(token, "move", "-4", "-10")

