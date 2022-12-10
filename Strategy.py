import gameGenerator as gg


global moveq
global mover
moveq = [0, 1, -1, 1, -1, 0]
mover = [-1, -1, 0, 0, 1 ,1]
# vraca 4 stvari (q,r, duzina puta, opponent)
def bossbfs(startq, startr, opponent):
    queue = [[startq, startr, 0]]
    while not len(queue) == 0:
        curq = queue[0][0]
        curr = queue[0][1]
        value = queue[0][2]
        queue.remove(0)
        for i in range(len(moveq)):

            if curq + moveq[i] >= 0 and curq + moveq[i] <= 14 and curr + mover[i] >= 0 and curr + mover[i] <= 14:
                appendval = game_map.get(curq + moveq[i] + ":" + curr + mover[i])
                newval = -1
                if appendval.get("type") == "NORMAL":
                    newval = 1
                elif appendval.get("type") == "BLACKHOLE":
                    newval = 3
                elif appendval.get("type") == "ASTEROID":
                    #newval = 1 +
                    pass
                queue.append([curq + moveq[i], curr + mover[i], value + 1]) #todo: proveri vrednost i dodaj to
        queue = sorted(queue, key=lambda x: x[2])
    #return "a + b", opponent
def regularbfs(startq, startr, q, r):
    pass

# pretpostavka je da smo jedan drugom u range-u i da se pucamo
def can_i_win(me, opponent):
    my_health = me['health']
    opponent_health = opponent['health']

    while True:
        opponent_health -= me['power']
        my_health -= opponent_health['power']

        # ako sam unutar boss zone
        if me['q'] >= -4 and me['q'] <= 4 and me['r'] >= -4 and me['r'] <= 4 and me['q'] + me['r'] >= -4 and me['q'] + me['r'] <= 4:
            my_health -= 250
            # ako je protivnik unutar boss zone
        if opponent['q'] >= -4 and opponent['q'] <= 4 and opponent['r'] >= -4 and opponent['r'] <= 4 and opponent['q'] + opponent['r'] >= -4 and opponent[
            'q'] + opponent['r'] <= 4:
            opponent_health -= 250

        if opponent_health <= 0:
            return True
        if my_health <= 0:
            return False


# closest_opponent ima u sebi q,r gde ulazi u boss zonu, razdaljinu do boss zone, i poslednji argument su sve ostale info o opponent-u
# treba da proverimo da li mozemo doci do njega i srediti ga na vreme kako bi uzeli poene
def can_i_get_in_time(me, closest_opponent):
    # poziva i can_i_win
    return True

def in_shooting_range(me, opponent):
    return True


global game_map
global objective_map
global bots_map
game_state_json = open('game_state_json2.json')
game_map, objective_map, bots_map = gg.create_hexagon_game_map(game_state_json.read())

# dodati da prosledjuje info o nama u mapi, a ne samo koordinate
def game_next_move(timespent, me):
    if timespent > 5: #todo:proceni
        if me['q'] >= -4 and me['q'] <= 4 and me['r'] >= -4 and me['r'] <= 4 and me['q'] + me['r'] >= -4 and me['q'] + me['r'] <= 4:
            return "SHOOT BOSS"
        else:
            # dodati sta ako smo blizu neprijatelja za range <= 3
            for opponent in bots_map:
                if(in_shooting_range(me, opponent)):
                    if(can_i_win(me, opponent)):
                        return "SHOOT BOT"
                    else:
                        return "RUNAWAY"

            newq, newr = bossbfs(me['q'], me['r'])
            if game_map.get(newq + ":" + newr) == "ASTEROID":
                return "SHOOT " + newq + ":" + newr
            else:
                return "MOVE " + newq + ":" + newr
    else:
        if me['q'] >= -4 and me['q'] <= 4 and me['r'] >= -4 and me['r'] <= 4 and me['q'] + me['r'] >= -4 and me['q'] + me['r'] <= 4:
            return "SHOOT BOSS"
        xpq, xpr = objective_map.get("EXPERIENCE")
        mydist, newq, newr = regularbfs(me['q'], me['r'], xpq, xpr)
        chasexpflag = True
        #Prvo gledamo da li smo najblizi xpu
        for opponent in bots_map:
            if regularbfs(opponent['q'], opponent['r'], xpq, xpr)[0] < mydist:
                chasexpflag = False
                break
        if chasexpflag == True:
            if game_map.get(newq + ":" + newr) == "ASTEROID":
                return "SHOOT " + newq + ":" + newr
            else:
                return "MOVE " + newq + ":" + newr
        bot_goals = [[]]
        for opponent in bots_map:
            bot_goals.append(bossbfs(opponent['q'], opponent['r'], opponent))

        # sortiramo po tome koliko su blizu boss-a
        sorted_bot_goals = sorted(bot_goals, key=lambda x: x[2])

        closest_opponent = sorted_bot_goals[0]
        if(can_i_get_in_time(me, closest_opponent)):
            # treba odrediti koordinate na koje treba otici
            return "MOVE" + "kordinate"

#         ako nista nije proslo onda idemo na boss-a
#         implementirati bfs da nam da kordinate za sledeci potez
        newq, newr = bossbfs(me['q'], me['r'])
        if game_map.get(newq + ":" + newr) == "ASTEROID":
            return "SHOOT " + newq + ":" + newr
        else:
            return "MOVE " + newq + ":" + newr

#         mozda dodati i neki random potez, ponekad

#         na kraju poteza staviti current_bot_positions na old_bot_decisions





q = []
game_map.get()