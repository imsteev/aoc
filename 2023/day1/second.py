input = []
with open('input.txt') as f:
    input = f.read().splitlines()

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

total = 0
for s in input:
    digits = extract_digits(s)
    total += int(digits[0]+digits[-1])

print(total)