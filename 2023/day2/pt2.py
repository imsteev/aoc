from .. import parse

GAMES = {}
for line in parse.read_input():

    game_str, rounds_str = line.split(': ')
    game_num = int(game_str.split(' ')[1])

    # each round looks like "17 red, 5 blue, 3 green"
    rounds = []
    for r in rounds_str.split('; '):

        # normalize the round into an object
        round = {}
        for cube in r.strip().split(', '):
            count, color = cube.split(' ')
            round[color] = int(count)

        rounds.append(round)

    GAMES[game_num] = rounds

"""
The "power" of a game is equal to the product of
the minimum count of each color needed to satisfy
each round.
"""
import functools

def power(game, colors):
    max_colors = {}
    for round in game:
        for color in round:
            # only track a color if necessary
            if color not in max_colors:
                max_colors[color] = 0

            # if there's a bigger count for a given color, choose that
            max_colors[color] = max(max_colors[color], round[color])

    return functools.reduce(lambda x,y: x*y, max_colors.values())



def calculate_answer():
    return sum(power(game, ['red', 'green', 'blue']) for game in GAMES.values())

print(calculate_answer())
