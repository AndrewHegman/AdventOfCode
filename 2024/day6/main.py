map = []
pos = [0, 0]
start = (0, 0)
obstacles = []
dir = "N"
positions_traveled = set()

with open("input.txt") as f:
    for row, line in enumerate(f):
        map.append([])
        for col, c in enumerate(line.rstrip()):
            if c == "^":
                pos = (row, col)
                start = (row, col)
            if c == "#":
                obstacles.append((row, col))
            map[row].append(c)


def get_nearest_obstacle(p):
    nearest_dist = 999999999
    nearest_obstacle = (-1, -1)

    for obstacle in obstacles:
        if (dir == "N" or dir == "S") and obstacle[1] == p[1]:
            if (
                dir == "N"
                and obstacle[0] < p[0]
                and get_distance(p, obstacle) < nearest_dist
            ):
                nearest_dist = get_distance(p, obstacle)
                nearest_obstacle = obstacle
            if (
                dir == "S"
                and obstacle[0] > p[0]
                and get_distance(p, obstacle) < nearest_dist
            ):
                nearest_dist = get_distance(p, obstacle)
                nearest_obstacle = obstacle

        if (dir == "E" or dir == "W") and obstacle[0] == p[0]:
            if (
                dir == "E"
                and obstacle[1] > p[1]
                and get_distance(p, obstacle) < nearest_dist
            ):
                nearest_dist = get_distance(p, obstacle)
                nearest_obstacle = obstacle
            if (
                dir == "W"
                and obstacle[1] < p[1]
                and get_distance(p, obstacle) < nearest_dist
            ):
                nearest_dist = get_distance(p, obstacle)
                nearest_obstacle = obstacle
    return nearest_obstacle


def do_move():
    global pos
    global dir

    nearest_obstacle = get_nearest_obstacle(pos)
    is_outside_map = False

    if nearest_obstacle == (-1, -1):
        if dir == "N":
            nearest_obstacle = (-1, pos[1])
        if dir == "E":
            nearest_obstacle = (pos[0], len(map[0]))
        if dir == "S":
            nearest_obstacle = (len(map), pos[1])
        if dir == "W":
            nearest_obstacle = (pos[0], -1)
        is_outside_map = True

    if dir == "N":
        pt = [(x, pos[1]) for x in range(nearest_obstacle[0] + 1, pos[0])]
        pos = (nearest_obstacle[0] + 1, pos[1])
        dir = "E"
        return (pt, is_outside_map)

    if dir == "E":
        pt = [(pos[0], x) for x in range(pos[1], nearest_obstacle[1] - 1)]
        pos = (pos[0], nearest_obstacle[1] - 1)
        dir = "S"
        return (pt, is_outside_map)

    if dir == "S":
        pt = [(x, pos[1]) for x in range(pos[0], nearest_obstacle[0] - 1)]
        pos = (nearest_obstacle[0] - 1, pos[1])
        dir = "W"
        return (pt, is_outside_map)

    if dir == "W":
        pt = [(pos[0], x) for x in range(nearest_obstacle[1] + 1, pos[1] + 1)]
        pos = (pos[0], nearest_obstacle[1] + 1)
        dir = "N"
        return (pt, is_outside_map)

    print("Something is wrong..")
    return ([], True)


def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def print_pos():
    for row, r in enumerate(map):
        for col, c in enumerate(r):
            char = c
            if (row, col) in positions_traveled:
                char = "X"
            if (row, col) == pos:
                char = get_cursor()
            elif c == "^":
                char = "."

            print(char, end="")
        print()


def get_cursor():
    if dir == "N":
        return "^"
    if dir == "E":
        return ">"
    if dir == "S":
        return "v"
    if dir == "W":
        return "<"


def check_for_loop():
    global pos
    global dir

    pos = start
    pos_set = []
    dir = "N"

    pos_set.append((pos, dir))
    tmp = do_move()
    while not tmp[1]:
        if len(tmp[0]) > 0:
            pos_set.append((pos, dir))
        tmp = do_move()

        if (pos, dir) in pos_set:
            return True
    return False


positions_traveled.update([pos])
tmp = do_move()
while not tmp[1]:
    positions_traveled.update(tmp[0])
    tmp = do_move()

positions_traveled.update(tmp[0])
positions_traveled.update([pos])
loops = 0

# Find loops
for position in positions_traveled:
    obstacles.append(position)
    # print(f"Testing {position} ({loops})")
    loops += 1 if check_for_loop() else 0
    obstacles.pop()


print("Part1: ", len(positions_traveled))
print("Part2: ", loops)
