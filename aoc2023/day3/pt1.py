
input = []
with open('input.txt', 'r') as f:
    input = f.read().splitlines()


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


DIRECTIONS = [(-1,-1), (-1, 0), (-1, +1), (0, +1), (+1, +1),(+1, 0),(+1,-1), (0, -1)]

# turn into 2d-array
grid = [list(l) for l in input]

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

print(total)