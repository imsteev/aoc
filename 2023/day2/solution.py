ACTUAL_COUNTS = {'red': 12, 'green': 13, 'blue': 14}  # this comes from your prompt

def parse_games(input):
    games = {}

    for line in input:

        # Parse game number
        game_str, rounds_str = line.split(': ')
        game_num = int(game_str.split(' ')[1])

        # A "round" is comprised of the counts of each color that the elf selected.
        rounds = []
        for r in rounds_str.split('; '):

            round = {}
            for cube in r.strip().split(', '):
                count, color = cube.split(' ')
                round[color] = int(count)

            rounds.append(round)

        games[game_num] = rounds

    return games


def does_round_pass(round, cube_counts):
    return all(count <= cube_counts[color] for color, count in round.items())

def part1(input):
    id_sum = 0
    for game_num, rounds in parse_games(input).items():
        all_rounds_pass = all(does_round_pass(round, ACTUAL_COUNTS) for round in rounds)
        if all_rounds_pass:
            id_sum += game_num
    return id_sum

"""
The "power" of a game is equal to the product of
the minimum count of each color needed to satisfy
each round.
"""
import functools

def power(game):
    max_colors = {}
    for round in game:
        for color in round:
            # only track a color if necessary
            if color not in max_colors:
                max_colors[color] = 0

            # if there's a bigger count for a given color, choose that
            max_colors[color] = max(max_colors[color], round[color])

    return functools.reduce(lambda x,y: x*y, max_colors.values())

def part2(input):
    games =  parse_games(input)
    return sum(power(game) for game in games.values())

if __name__ == '__main__':
    input = []
    with open('input.txt', 'r') as f:
        input = f.read().splitlines()

    print(f'answer to part 1: {part1(input)}')
    print(f'answer to part 2: {part2(input)}')
