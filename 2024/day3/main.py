import sys
import re

is_test = len(sys.argv) > 1 and sys.argv[1] == "--test"
part1_answer = 161
part2_answer = 48

part1 = 0
part2 = 0


def do_multiply(str):
    return sum(
        [int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", "".join(str))]
    )


with open("test.txt" if is_test else "input.txt", "r") as f:
    txt = f.read()
    part1 = do_multiply(txt)
    enabled_expressions = [x.split("don't()")[0] for x in txt.split("do()")]
    part2 = do_multiply(enabled_expressions)


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
