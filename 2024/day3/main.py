import sys

is_test = len(sys.argv) > 1 and sys.argv[1] == "--test"
part1_answer = None
part2_answer = None

part1 = None
part2 = None

with open("test.txt" if is_test else "input.txt", "r") as f:
    pass

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
