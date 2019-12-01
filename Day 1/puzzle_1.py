with open("Day 1/input.txt", "r") as f:
    lines = [int(k) for k in f.readlines()]

total = 0
for num in lines:
    total += (num // 3) - 2
print(total)
