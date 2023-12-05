import re

def part1(input):
    total_pts = 0

    for line in input:
        scorecard = line.split(': ')[1]
        winning_nums_str, my_nums_str = scorecard.split(' | ')

        # numbers are "justified", so we need to split on whitespace, not just a single space.
        winning_nums = re.split(r'\s+', winning_nums_str.strip())
        my_nums = re.split(r'\s+', my_nums_str.strip())

        my_winning_nums = [num for num in my_nums if num in winning_nums]

        # score starts at 1, doubling with each subsequent winning number.
        if len(my_winning_nums) > 0:
            score = 2**(len(my_winning_nums)-1)
            total_pts += score

    return total_pts

def part2(input):

    matches_by_card = {}  # int -> int
    for line in input:
        # whole lotta parsing :woozy
        card, scorecard  = line.split(': ')
        card_num = re.split(r'\s+', card)[1]
        winning_nums_str, my_nums_str = scorecard.split(' | ')

        my_nums = re.split(r'\s+', my_nums_str.strip())
        winning_nums = re.split(r'\s+', winning_nums_str.strip())

        my_winning_nums = [num for num in my_nums if num in winning_nums]

        matches_by_card[int(card_num)] = len(my_winning_nums)

    seen = {}
    total_copies = 0
    for i in range(1, len(matches_by_card)+1):
        # Make sure we do not double-count
        if i not in seen:
            total_copies += find_copies(i, matches_by_card)

    # total cards = total copies + total # of originals
    return total_copies + len(matches_by_card)


def find_copies(card_num, matches_by_card):
    if matches_by_card[card_num] == 0:
        # no winning numbers, no copies.
        return 0

    # Recursively find copies of card_num's copies.
    # The prompt defines these as the next len(winning_numbers) of cards
    # and is guaranteed to not go beyond the input length.
    copies = matches_by_card[card_num]
    for i in range(card_num+1, card_num+1+copies):
        copies += find_copies(i, matches_by_card)

    return copies

if __name__ == '__main__':
    input = []
    with open('input.txt', 'r') as f:
        input = f.read().splitlines()

    print(f'answer to part 1: {part1(input)}')
    print(f'answer to part 2: {part2(input)}')