from math import atan, degrees, sqrt
from collections import defaultdict
import sys

asteriod_map = []

with open("Day 10/input.txt", "r") as f:
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            if char == "#":
                asteriod_map.append((x, y))


def calculate_angle(starting_asteroid, asteroid):
    dx = asteroid[0] - starting_asteroid[0]
    dy = asteroid[1] - starting_asteroid[1]

    try:
        if dx < 0 and dy == 0:
            return 270
        elif dx > 0 and dy == 0:
            return 90
        elif dx == 0 and dy > 0:
            return 180
        elif dx == 0 and dy < 0:
            return 0
        else:
            angle = abs(degrees(atan(dy/dx)))

        # 2. Quadrant
        if dx < 0 and dy < 0:
            angle = 270 + angle

        # 3. Quadrant
        elif dx < 0 and dy > 0:
            angle = 270 - angle

        # 4. Quadrant
        elif dx > 0 and dy > 0:
            angle = 90 + angle

        # 1. Quadrant
        elif dx > 0 and dy < 0:
            angle = 90 - angle

    except ZeroDivisionError:
        angle = 0 if dy < 0 else 180

    return angle


def distance(vec1: tuple, vec2: tuple):
    return sqrt(
        (vec1[0] - vec2[0])**2 + (vec1[1] - vec2[1])**2
    )


def calculate_angles_for_asteroids(starting_asteroid: tuple):
    d = defaultdict(list)
        
    for asteroid in filter(lambda ast: ast != starting_asteroid, asteriod_map):
        angle = calculate_angle(starting_asteroid, asteroid)
        d[angle].append((asteroid, distance(asteroid, starting_asteroid)))

    return d


def get_closest(d: dict):
    res = []
    for angle, asteroids in d.items():
        res.append(
            (angle, min(asteroids, key=lambda o: o[1]))
        )

    res = sorted(res, key=lambda o: o[0])
    return res


if __name__ == "__main__":
    assert calculate_angle((8, 3), (9, 2)) == 45
    assert calculate_angle((8, 3), (10, 4)) == 116.56505117707799
    assert calculate_angle((8, 3), (4, 4)) == 255.96375653207352
    assert calculate_angle((8, 3), (7, 0)) == 341.565051177078
    assert calculate_angle((8, 3), (8, 1)) == 0
    assert calculate_angle((8, 3), (8, 4)) == 180
    assert calculate_angle((8, 3), (12, 3)) == 90
    assert calculate_angle((8, 3), (2, 3)) == 270
    
    pos = (23, 29)
    res = calculate_angles_for_asteroids(pos)
    
    deleted = 0
    while True:
        closest_asteroids = get_closest(res)
        for ast_angle, ast in closest_asteroids:
            ast_pos, ast_distance = ast
    
            del res[ast_angle]
            deleted += 1
            print(deleted, "asteroid", ast_pos)

            if deleted == 200:
                print("RESULT", ast_pos[0] * 100 + ast_pos[1])
                sys.exit()
