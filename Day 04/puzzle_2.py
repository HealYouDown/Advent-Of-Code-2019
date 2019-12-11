def check_if_number_is_decreasing(number: int):
    number_s = str(number)
    for num1, num2 in zip(number_s, number_s[1:]):
        if num2 < num1:
            return False
    return True


def contains_pair(number: int):
    number_s = str(number)
    return any(pair in number_s for pair in [str(i)+str(i) for i in range(0, 10)])


def has_legal_number_of_pairs(number: int):
    number_s = str(number)
    counts = set(number_s.count(char) for char in number_s)
    if not 2 in counts and any(val > 2 for val in counts):
        return False
    return True


matching_numbers = set()

for number in range(265275, 781584+1):
    if not check_if_number_is_decreasing(number):
        continue

    if not contains_pair(number):
        continue

    if not has_legal_number_of_pairs(number):
        continue

    matching_numbers.add(number)

print(len(matching_numbers))
