from IPython.display import clear_output

game_props = {
    "currently_playing": True,
    "board": [],
    "emptypositions": [],
    "finishedgame": False,
    "player1": {
        "name": '',
        "marker": ''
    },
    "player2": {
        "name": '',
        "marker": ''
    }
}


def init_gameboard():
    for count in range(9):
        game_props["board"].append('*')
    # return game_props["board"]


def generate_gamedisplay():
    clear_output()
    print(' --- | --- | --- ')
    print('  {}  |  {}  |  {}  '.format(
        game_props["board"][0], game_props["board"][1], game_props["board"][2]
    ))
    print(' -1- | -2- | -3- ')
    print('  {}  |  {}  |  {}  '.format(
        game_props["board"][3], game_props["board"][4], game_props["board"][5]
    ))
    print(' -4- | -5- | -6- ')
    print('  {}  |  {}  |  {}  '.format(
        game_props["board"][6], game_props["board"][7], game_props["board"][8]
    ))
    print(' -7- | -8- | -9- ')


def init_players():
    while game_props["player1"]["name"] == '' or game_props["player1"]["name"] == ' ':
        game_props["player1"]["name"] = input(
            'Hi Player 1, What is your name?\n')
    while game_props["player1"]["marker"] != 'X' and game_props["player1"]["marker"] != 'O':
        game_props["player1"]["marker"] = input(
            'Type O to be noughts or X to be crosses\n').upper()
    if game_props["player1"]["marker"] == 'O':
        game_props["player2"]["marker"] = 'X'
    else:
        game_props["player2"]["marker"] = 'O'
    while game_props["player2"]["name"] == '' or game_props["player2"]["name"] == ' ':
        game_props["player2"]["name"] = input(
            'Hi Player 2, What is your name?\n')


def state_playerstats():
    print(
        f'{game_props["player1"]["name"]} is {game_props["player1"]["marker"]}')
    print(
        f'{game_props["player2"]["name"]} is {game_props["player2"]["marker"]}')


def check_empty_positions():
    update_list = []
    for index, position in enumerate(game_props["board"]):
        if position == "*":
            update_list.append(index+1)
        else:
            continue
    game_props["emptypositions"] = update_list


def emptyposition_render():
    render_string = ""
    for position in game_props["emptypositions"]:
        render_string += " | " + str(position) + " | "
    return render_string


def player_choice(player):
    choice = None
    print(f'{player["name"]}, It\'s your turn!')
    while type(choice) != int:
        while choice not in game_props["emptypositions"]:
            print(f'Available positions: {emptyposition_render()}')
            try:
                choice = int(input(
                    f'Enter the number of an available position to place your {player["marker"]}\n'))
            except:
                print("That is not a valid number, try again")
    game_props["board"][choice-1] = player["marker"]


def win_query(player):
    board = game_props["board"]
    marker = player["marker"]
    '''
    0,1,2 + 0,3,6 + 0,4,8 + 1,4,7 + 2,4,6 + 2,5,8 + 3,4,5 + 6,7,8
    '''
    if board[0] + board[1] + board[2] == marker*3:
        announce_winner(player)
    elif board[0] + board[3] + board[6] == marker*3:
        announce_winner(player)
    elif board[0] + board[4] + board[8] == marker*3:
        announce_winner(player)
    elif board[1] + board[4] + board[7] == marker*3:
        announce_winner(player)
    elif board[2] + board[4] + board[6] == marker*3:
        announce_winner(player)
    elif board[2] + board[5] + board[8] == marker*3:
        announce_winner(player)
    elif board[3] + board[4] + board[5] == marker*3:
        announce_winner(player)
    elif board[6] + board[7] + board[8] == marker*3:
        announce_winner(player)
    elif "*" not in game_props["board"]:
        announce_tie()
    else:
        pass


def announce_winner(player):
    generate_gamedisplay()
    print(f'{player["name"]} who plays as {player["marker"]} has won')
    game_props["finishedgame"] = True


def announce_tie():
    generate_gamedisplay()
    print('Looks like the game has ended with a tie!')
    game_props["finishedgame"] = True


def quit_game():
    game_props["currently_playing"] = False
    print('Thank you for playing!')


def replay_query():
    answer = ""
    while answer != 'Y' and answer != 'N':
        answer = input(
            'Would you like to start a new game? Y for yes, N for no\n').upper()
    if answer == 'Y':
        game_props["finishedgame"] = False
    else:
        quit_game()


def continue_query():
    answer = ""
    while answer == "":
        while answer != 'Y' and answer != 'N':
            answer = input(
                'Would you like to continue playing? Y for yes, N for no\n').upper()
        if answer == 'Y':
            continue
        else:
            game_props["finishedgame"] = True
            break


def player_turn(player):
    generate_gamedisplay()
    check_empty_positions()
    player_choice(player)
    win_query(player)


def turn_phase():
    while game_props["finishedgame"] == False:
        continue_query()
        if game_props["finishedgame"] == False:
            player_turn(game_props["player1"])
        else:
            break
        if game_props["finishedgame"] == False:
            player_turn(game_props["player2"])
        else:
            break


def reset_game():
    game_props["board"] = []
    game_props["emptypositions"] = []
    game_props["player1"] = {
        "name": '',
        "marker": ''
    }
    game_props["player2"] = {
        "name": '',
        "marker": ''
    }


def init_game():
    reset_game()
    init_gameboard()
    init_players()
    state_playerstats()


def run():
    while game_props["currently_playing"]:
        init_game()
        turn_phase()
        replay_query()


run()
