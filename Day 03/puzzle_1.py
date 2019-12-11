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

# Get all points where the wire goes
points_wire_1 = get_points(moves_wire_1)
points_wire_2 = get_points(moves_wire_2)

# Find the points that are the same in both list
in_both = [p for p in points_wire_2 if p in points_wire_1]

# Find the closest one from the start
distances = [abs(x)+abs(y) for x, y in in_both]
print(min(distances))
