input = []
with open('input.txt') as f:
    input = f.read().splitlines()

total = 0
for s in input:
    digits = [c for c in s if c.isdigit()]
    total += int(digits[0] + digits[-1])

print("total: " + str(total))