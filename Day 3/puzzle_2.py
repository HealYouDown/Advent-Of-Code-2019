with open("Day 3/input.txt", "r") as f:
    lines = f.readlines()
    moves_wire_1 = lines[0].split(",")
    moves_wire_2 = lines[1].split(",")

def get_points(moveset: list):
    current_x = 0
    current_y = 0

    points = set()

    for move in moveset:
        direction = move[:1]
        steps = int(move[1:])

        if direction == "R":
            line_points = [(current_x + i, current_y) for i in range(1, steps+1)]
            points.update(line_points)
            current_x += steps

        elif direction == "L":
            line_points = [(current_x - i, current_y) for i in range(1, steps+1)]
            points.update(line_points)
            current_x -= steps

        elif direction == "D":
            line_points = [(current_x, current_y - i) for i in range(1, steps+1)]
            points.update(line_points)
            current_y -= steps

        elif direction == "U":
            line_points = [(current_x, current_y + i) for i in range(1, steps+1)]
            points.update(line_points)
            current_y += steps

    return points


def count_to_intersection(intersection: tuple, moveset: list):
    """Returns total steps needed to reach the intersection."""
    total_steps = 0
    current_x = 0
    current_y = 0

    points = []

    for move in moveset:
        direction = move[:1]
        steps = int(move[1:])

        if direction == "R":
            line_points = [(current_x + i, current_y) for i in range(1, steps+1)]
            points.extend(line_points)
            current_x += steps

        elif direction == "L":
            line_points = [(current_x - i, current_y) for i in range(1, steps+1)]
            points.extend(line_points)
            current_x -= steps

        elif direction == "D":
            line_points = [(current_x, current_y - i) for i in range(1, steps+1)]
            points.extend(line_points)
            current_y -= steps

        elif direction == "U":
            line_points = [(current_x, current_y + i) for i in range(1, steps+1)]
            points.extend(line_points)
            current_y += steps
        
        if intersection in points:
            return points.index(intersection) + 1
        
# Get all points where the wire goes
points_wire_1 = get_points(moves_wire_1)
points_wire_2 = get_points(moves_wire_2)

# Find the points that are the same in both list
intersections = [p for p in points_wire_2 if p in points_wire_1]

# Go through all intersections and recaculate how many steps for each wire
# are needed to reach that intersection
total_steps_to_intersections = []

for intersection in intersections:
    print(intersection)
    steps_wire_1 = count_to_intersection(intersection, moves_wire_1)
    steps_wire_2 = count_to_intersection(intersection, moves_wire_2)
    
    total_steps_to_intersections.append(steps_wire_1 + steps_wire_2)

print(min(total_steps_to_intersections))
