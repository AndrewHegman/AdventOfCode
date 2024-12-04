def check_n(s, pos, letter) -> int:
    if pos[0] - 1 >= 0 and s[pos[0] - 1][pos[1]] == letter:
        return 1
    return 0


def check_ne(s, pos, letter):
    if (
        pos[0] - 1 >= 0
        and pos[1] + 1 <= len(s) - 1
        and s[pos[0] - 1][pos[1] + 1] == letter
    ):
        return 1
    return 0


def check_e(s, pos, letter):
    if pos[1] + 1 <= len(s) - 1 and s[pos[0]][pos[1] + 1] == letter:
        return 1
    return 0


def check_se(s, pos, letter):
    if (
        pos[0] + 1 <= len(s) - 1
        and pos[1] + 1 <= len(s) - 1
        and s[pos[0] + 1][pos[1] + 1] == letter
    ):
        return 1
    return 0


def check_s(s, pos, letter):
    if pos[0] + 1 <= len(s) - 1 and s[pos[0] + 1][pos[1]] == letter:
        return 1
    return 0


def check_sw(s, pos, letter):
    if (
        pos[0] + 1 <= len(s) - 1
        and pos[1] - 1 >= 0
        and s[pos[0] + 1][pos[1] - 1] == letter
    ):
        return 1
    return 0


def check_w(s, pos, letter):
    if pos[1] - 1 >= 0 and s[pos[0]][pos[1] - 1] == letter:
        return 1
    return 0


def check_nw(s, pos, letter):
    if pos[0] - 1 >= 0 and pos[1] - 1 >= 0 and s[pos[0] - 1][pos[1] - 1] == letter:
        return 1
    return 0
