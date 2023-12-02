input = []
with open('input.txt', 'r') as f:
    input = f.read().splitlines()


"""
Example line looks like:

Game 5: 17 red, 5 blue, 3 green; 8 green, 9 red, 10 blue; 2 green, 9 blue, 4 red

"""
GAMES = {}

for line in input:

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
the "power" of a game is equal to the product of the minimum count of each color needed
to satisfy each round.
"""
def power(game, colors):
    max_colors = {}
    for round in game:
        for color in colors:
            if color not in round:
                continue

            # only track a color if necessary
            if color not in max_colors:
                max_colors[color] = 0

            # if there's a bigger count for a given color, choose that
            max_colors[color] = max(max_colors[color], round[color])

    power = 1

    for color_max in max_colors.values():
        power *= color_max

    return power

power_sum = 0
for game_num, game in GAMES.items():
    power_sum += power(game, ['red', 'green', 'blue'])

print(power_sum)