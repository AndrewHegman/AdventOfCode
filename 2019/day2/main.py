import copy

data = []
part1 = None
part2 = None


def execute(pc):
    global data
    # print(pc)
    if data[pc] == 1:
        data[data[pc + 3]] = data[data[pc + 1]] + data[data[pc + 2]]
    elif data[pc] == 2:
        data[data[pc + 3]] = data[data[pc + 1]] * data[data[pc + 2]]
    elif data[pc] == 99:
        # print("Program finished")
        return -1


with open("input.txt") as f:
    original = [int(x) for x in f.read().split(",")]
    data = copy.deepcopy(original)
    data[1] = 12
    data[2] = 2

    pc = 0

    while execute(pc) != -1:
        pc += 4

    part1 = data[0]
    part2_finished = False
    for i in range(100):
        for j in range(100):

            f.seek(0)
            data = [int(x) for x in f.read().split(",")]
            pc = 0
            data[1] = i
            data[2] = j

            while execute(pc) != -1:
                pc += 4

            if data[0] == 19690720:
                part2 = 100 * data[1] + data[2]

                part2_finished = True
                break
        if part2_finished:
            break

print("Part1: ", part1)
print("Part2: ", part2)
