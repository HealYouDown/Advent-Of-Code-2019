from math import tan, atan, degrees

asteriod_map = []

with open("Day 10/input.txt", "r") as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            if char == "#":
                asteriod_map.append((x, y))


def calculate_visible_asteroids(starting_asteroid: tuple):
    angles = set()
    for asteroid in filter(lambda ast: ast != starting_asteroid, asteriod_map):
        dx = asteroid[0] - starting_asteroid[0]
        dy = asteroid[1] - starting_asteroid[1]

        try:
            if dx < 0 and dy == 0:
                angle = 270
            elif dx > 0 and dy == 0:
                angle = 90
            else:
                angle = degrees(atan(tan(dy/dx)))

            if dx < 0 and dy < 0:
                angle += 270
            elif dx < 0 and dy > 0:
                angle += 180
            elif dx > 0 and dy > 0:
                angle += 90
            elif dx > 0 and dy < 0:
                angle = abs(angle)

        except ZeroDivisionError:
            angle = 0 if dy < 0 else 180       

        angles.add(angle)

    return len(angles)

if __name__ == "__main__":
    results = {}
    for asteroid in asteriod_map:
        results[asteroid] = calculate_visible_asteroids(asteroid)
    
    max_asteroids_seen = 0
    max_asteroids_seen_pos = None
    
    for pos, asteroids_seen in results.items():
        if asteroids_seen > max_asteroids_seen:
            max_asteroids_seen = asteroids_seen
            max_asteroids_seen_pos = pos
    
    print(max_asteroids_seen_pos, max_asteroids_seen)
