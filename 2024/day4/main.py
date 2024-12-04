import sys
import utils

is_test = len(sys.argv) > 1 and sys.argv[1] == "--test"
part1_answer = 18
part2_answer = 9

part1 = 0
part2 = 0

word_search = []


def check_ne_sw(pos):
    if (
        utils.check_ne(word_search, (pos[0], pos[1]), "M")
        and utils.check_sw(word_search, (pos[0], pos[1]), "S")
    ) or (
        utils.check_ne(word_search, (pos[0], pos[1]), "S")
        and utils.check_sw(word_search, (pos[0], pos[1]), "M")
    ):
        return 1
    return 0


def check_nw_se(pos):
    if (
        utils.check_nw(word_search, (pos[0], pos[1]), "M")
        and utils.check_se(word_search, (pos[0], pos[1]), "S")
    ) or (
        utils.check_nw(word_search, (pos[0], pos[1]), "S")
        and utils.check_se(word_search, (pos[0], pos[1]), "M")
    ):
        return 1
    return 0


def check_n_mas(pos):
    if (
        utils.check_n(word_search, (pos[0], pos[1]), "M")
        and utils.check_n(word_search, (pos[0] - 1, pos[1]), "M")
        and utils.check_n(word_search, (pos[0] - 2, pos[1]), "M")
    ):
        return 1
    return 0


def check_ne_mas(pos):
    if (
        utils.check_ne(word_search, (pos[0], pos[1]), "M")
        and utils.check_ne(word_search, (pos[0] - 1, pos[1] + 1), "A")
        and utils.check_ne(word_search, (pos[0] - 2, pos[1] + 2), "S")
    ):
        return 1
    return 0


def check_e_mas(pos):
    if (
        utils.check_e(word_search, (pos[0], pos[1]), "M")
        and utils.check_e(word_search, (pos[0], pos[1] + 1), "A")
        and utils.check_e(word_search, (pos[0], pos[1] + 2), "S")
    ):
        return 1
    return 0


def check_se_mas(pos):
    if (
        utils.check_se(word_search, (pos[0], pos[1]), "M")
        and utils.check_se(word_search, (pos[0] + 1, pos[1] + 1), "A")
        and utils.check_se(word_search, (pos[0] + 2, pos[1] + 2), "S")
    ):
        return 1
    return 0


def check_s_mas(pos):
    if (
        utils.check_s(word_search, (pos[0], pos[1]), "M")
        and utils.check_s(word_search, (pos[0] + 1, pos[1]), "A")
        and utils.check_s(word_search, (pos[0] + 2, pos[1]), "S")
    ):
        return 1
    return 0


def check_sw_mas(pos):
    if (
        utils.check_sw(word_search, (pos[0], pos[1]), "M")
        and utils.check_sw(word_search, (pos[0] + 1, pos[1] - 1), "A")
        and utils.check_sw(word_search, (pos[0] + 2, pos[1] - 2), "S")
    ):
        return 1
    return 0


def check_w_mas(pos):
    if (
        utils.check_w(word_search, (pos[0], pos[1]), "M")
        and utils.check_w(word_search, (pos[0], pos[1] - 1), "A")
        and utils.check_w(word_search, (pos[0], pos[1] - 2), "S")
    ):
        return 1
    return 0


def check_nw_mas(pos):
    if (
        utils.check_e(word_search, (pos[0], pos[1]), "M")
        and utils.check_e(word_search, (pos[0] - 1, pos[1] - 1), "A")
        and utils.check_e(word_search, (pos[0] - 2, pos[1] - 2), "S")
    ):
        return 1
    return 0


with open("test.txt" if is_test else "input.txt", "r") as f:
    for line in f:
        word_search.append(list(line.strip()))

    for i in range(len(word_search)):
        for j in range(len(word_search[i])):
            if word_search[i][j] == "X":
                part1 += (
                    check_n_mas((i, j))
                    + check_ne_mas((i, j))
                    + check_e_mas((i, j))
                    + check_se_mas((i, j))
                    + check_s_mas((i, j))
                    + check_sw_mas((i, j))
                    + check_w_mas((i, j))
                    + check_nw_mas((i, j))
                )
            if word_search[i][j] == "A":
                part2 += (check_ne_sw((i, j)) + check_nw_se((i, j))) // 2


print()
if is_test:
    print(f"Expected: {part1_answer}")
    print(f"Got: {part1}")
    print("PASS" if part1 == part1_answer else "FAIL")
else:
    print("Part1:", part1)

print()
if is_test:
    print(f"Expected: {part2_answer}")
    print(f"Got: {part2}")
    print("PASS" if part2 == part2_answer else "FAIL")
else:
    print("Part2: ", part2)
print()
