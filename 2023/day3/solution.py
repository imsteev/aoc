def get_number_and_mark_seen(row, start_pos):
    num_str = str(row[start_pos])
    row[start_pos] = '.'

    left = start_pos-1
    right = start_pos+1

    while left >= 0 and row[left].isdigit():
        num_str = row[left] + num_str
        row[left] = '.'
        left -= 1
    while right < len(row) and row[right].isdigit():
        num_str += row[right]
        row[right] = '.'
        right += 1

    return int(num_str)


# up-left, up, up-right, right, etc. In total 8 directions.
DIRECTIONS = [(-1,-1), (-1, 0), (-1, +1), (0, +1), (+1, +1),(+1, 0),(+1,-1), (0, -1)]

# turn into 2d-array
def parse_schematic(input):
    return [list(l) for l in input]

def part1(input):
    """
    Find all the numbers adjacent to a symbol (any non-digit, non-period character)
    and add them together. Once a number is used, it cannot be used again.
    """
    grid = parse_schematic(input)
    len_y = len(grid)
    len_x = len(grid[0])

    total = 0
    for i in range(len_y):
        for j in range(len_x):
            if grid[i][j] != '.' and not grid[i][j].isdigit(): # encountered a symbol
                # figure out if there are any part numbers around this symbol
                for dy, dx in DIRECTIONS:
                    y, x = i+dy, j+dx
                    if y >= 0 and y < len_y and x >= 0 and x < len_x and grid[y][x].isdigit():
                        total += get_number_and_mark_seen(grid[y], x)
    return total


def part2(input):
    """
    Find all the numbers adjacent to a gear ("*").
    Only add the gear ratio if the length of these numbers is equal to 2.
    """
    grid = parse_schematic(input)
    len_y = len(grid)
    len_x = len(grid[0])

    total = 0
    for i in range(len_y):
        for j in range(len_x):
            if grid[i][j] == '*': # encountered a gear

                parts = []

                # figure out if there are any part numbers around this symbol
                for dy, dx in DIRECTIONS:
                    y, x = i+dy, j+dx
                    if y >= 0 and y < len_y and x >= 0 and x < len_x and grid[y][x].isdigit():
                        parts.append(get_number_and_mark_seen(grid[y], x))

                if len(parts) == 2:
                    total += (parts[0]*parts[1])

    return total


if __name__ == '__main__':
    input = []
    with open('input.txt', 'r') as f:
        input = f.read().splitlines()

    print(f'answer to part 1: {part1(input)}')
    print(f'answer to part 2: {part2(input)}')
