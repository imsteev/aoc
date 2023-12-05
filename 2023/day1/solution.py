def part1(input):
    total = 0
    for s in input:
        digits = [c for c in s if c.isdigit()]
        total += int(digits[0] + digits[-1])
    return total


numbers_to_num = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

# todo: do this with less memory
def extract_digits(s):
    digits = []
    for i in range(len(s)):
        if s[i].isdigit():
            digits.append(s[i])
        else:
            prefix = s[i:]
            digits += [str(num) for num_word, num in numbers_to_num.items() if prefix.startswith(num_word)]

    return digits

def part2(input):
    total = 0
    for s in input:
        digits = extract_digits(s)
        total += int(digits[0]+digits[-1])

    return total

if __name__ == '__main__':
    input = []
    with open('input.txt', 'r') as f:
        input = f.read().splitlines()

    print(f'answer to part 1: {part1(input)}')
    print(f'answer to part 2: {part2(input)}')
