from collections import defaultdict

with open("Day 6/input.txt", "r") as f:
    data = f.readlines()


def calc(orbit_name: str, num=0) -> int:
    try:
        orbit_obj = next(filter(lambda tup: orbit_name in tup[1], orbits.items()))
    except StopIteration:  # nothing found
        return num

    num += 1
    return calc(orbit_obj[0], num)


orbits = defaultdict(list)
for line in data:
    orbit_inner, orbit_outer = line.strip().split(")")
    orbits[orbit_inner].append(orbit_outer)


# Create a set with all names of the orbits to loop over
unique_orbits = set()
for key, parent_orbits in orbits.items():
    unique_orbits.add(key)
    unique_orbits.update(parent_orbits)


# Calculate the total
total = 0
for orbit_name in unique_orbits:
    total += calc(orbit_name)
