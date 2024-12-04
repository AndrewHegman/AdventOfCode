import sys

is_test = len(sys.argv) > 1 and sys.argv[1] == "--test"
part1_answer = 2
part2_answer = 4

part1 = 0
part2 = 0


def is_safe(levels):
    if levels[0] == levels[1]:
        return False

    is_increasing = levels[0] < levels[1]
    previous_value = None

    for level in levels:
        value = int(level)
        if previous_value is not None:

            # Level must increase or decrease
            if value == previous_value:
                return False

            # Level must not increase or decrease by more than 3
            if abs(value - previous_value) > 3:
                return False

            # Level must consistently increase or decrease
            if (previous_value < value and not is_increasing) or (
                previous_value > value and is_increasing
            ):
                return False

        previous_value = value
    return True


with open("test.txt" if is_test else "input.txt", "r") as f:
    for line in f.readlines():
        levels = [int(x) for x in line.split(" ")]

        if is_safe(levels):
            part1 += 1
            part2 += 1
        else:
            for x in range(len(levels)):
                if is_safe([*levels[:x], *levels[x + 1 :]]):
                    part2 += 1
                    break


print("")
if is_test:
    print(f"Expected: {part1_answer}")
    print(f"Got: {part1}")
    print("PASS" if part1 == part1_answer else "FAIL")
else:
    print("Part1: ", part1)

print("")
if is_test:
    print(f"Expected: {part2_answer}")
    print(f"Got: {part2}")
    print("PASS" if part2 == part2_answer else "FAIL")
else:
    print("Part2: ", part2)
print("")
