game_props = {
    "board": [],
    "player1": {
        "name": "",
        "marker": ""
    },
    "player2": {
        "name": "",
        "marker": ""
    }
}



def init_gameboard() :
    for count in range(9) :
        game_props["board"].append(" ")
    return game_props["board"]

def generate_gamedisplay() :
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