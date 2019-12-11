with open("Day 1/input.txt", "r") as f:
    lines = [int(k) for k in f.readlines()]

def calculate_fuel(total_module_fuel, j):
    a = (j // 3) - 2
    if a <= 0:
        return total_module_fuel
    else:
        return calculate_fuel(total_module_fuel + a, a)

total = 0
for num in lines:
    total += calculate_fuel(total_module_fuel=0, j=num)
print(total)
