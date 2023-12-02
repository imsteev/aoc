"""
Cubes: red, green, blue

Goal:
Determine which games would have been possible
if the bag had been loaded with only
12 red cubes, 13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?


Each game:
 - game ID
 - x blue, y red, z green; etc. (few times per game)


Initial thoughts:
- you already know how many cubes there are for each color
- for each game
    for each round, make sure all cube colors have count <= ACTUAL_COUNT[color]

    if all rounds are valid, add the game number to the result

def is_possible(game, max_colors) -> bool:
    return False
"""

input = []
with open('input.txt', 'r') as f:
    input = f.read().splitlines()

GAMES = {}

"""
Example line looks like:

Game 5: 17 red, 5 blue, 3 green; 8 green, 9 red, 10 blue; 2 green, 9 blue, 4 red

"""
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


def does_round_pass(round, actual_color_counts):
    return all(count <= actual_color_counts[color] for color, count in round.items())

ACTUAL_COUNTS = {'red': 12, 'green': 13, 'blue': 14}
id_sum = 0
for game_num, rounds in GAMES.items():
    all_rounds_pass = all(does_round_pass(round, ACTUAL_COUNTS) for round in rounds)
    if all_rounds_pass:
        id_sum += game_num
