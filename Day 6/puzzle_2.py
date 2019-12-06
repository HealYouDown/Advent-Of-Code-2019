from collections import defaultdict

with open("Day 6/input.txt", "r") as f:
    data = f.readlines()


orbits = defaultdict(list)
for line in data:
    orbit_inner, orbit_outer = line.strip().split(")")
    orbits[orbit_inner].append(orbit_outer)


def find_inner_orbits(orbit_name: str, orbits_found=[]):
    try:
        inner_orbit = next(filter(lambda o: orbit_name in o[1], orbits.items()))
    except StopIteration:
        return list(reversed(orbits_found))
    
    orbits_found.append(inner_orbit)
    
    return find_inner_orbits(inner_orbit[0], orbits_found)


a = find_inner_orbits("YOU", [])
b = find_inner_orbits("SAN", [])

sames = [j for j in a if j in b]

connect_point = sames[-1]

new_a = a[a.index(connect_point):]
new_b = b[b.index(connect_point):]

# -1 because connect point is in it both lists
# and the other -1 because it works like that (see example)
print(len(new_a) + len(new_b) - 2)
