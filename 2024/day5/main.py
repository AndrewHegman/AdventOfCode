"""
I'm not exactly proud of this solution, but it works, so why fix what ain't broke, right? Who needs to be proud of their code anyway?
"""

ruleset = []
updates = []
invalid_updates = []


def get_input():
    global ruleset
    global updates
    with open("input.txt", "r") as f:
        line = f.readline()
        while line != "\n":
            ruleset.append([x.rstrip("\n") for x in line.split("|")])
            line = f.readline()

        line = f.readline()

        while line:
            updates.append([x.rstrip("\n") for x in line.split(",")])
            line = f.readline()


def fix_invalid():
    valid_updates = []
    made_change = True
    while made_change:
        for update in invalid_updates:
            valid = True
            made_change = False

            for rule in ruleset:
                found_first = -1
                found_second = -1

                if not valid:
                    break

                for idx, page in enumerate(update):
                    if page == rule[0]:
                        found_first = idx

                        # Found second before first, invalid update
                        if found_second >= 0:
                            valid = False
                            invalid_updates.append(update)

                            update.insert(idx + 1, rule[1])
                            del update[found_second]
                            made_change = True
                        # Found first before second, valid update
                        else:
                            break

                    if page == rule[1]:
                        found_second = idx

                        # Found second before first, invalid update
                        if found_first >= 0:
                            valid = False
                            invalid_updates.append(update)

                            update.insert(found_first + 1, rule[1])
                            del update[found_second]
                            made_change = True

            if valid:
                valid_updates.append(update[len(update) // 2])

    return valid_updates


def execute(part2):
    valid_updates = []

    for update in updates:
        valid = True

        for rule in ruleset:
            found_first = -1
            found_second = -1

            if not valid and not part2:
                break

            for idx, page in enumerate(update):
                if page == rule[0]:
                    found_first = idx

                    # Found second before first, invalid update
                    if found_second >= 0:
                        valid = False
                        invalid_updates.append(update)
                        if not part2:
                            break

                        update.insert(idx + 1, rule[1])
                        del update[found_second]

                    # Found first before second, valid update
                    else:
                        break

                if page == rule[1]:
                    found_second = idx

                    # Found second before first, invalid update
                    if found_first >= 0:
                        valid = False
                        invalid_updates.append(update)
                        if not part2:
                            break

                        update.insert(found_first + 1, rule[1])
                        del update[found_second]

        if not part2 and valid:
            valid_updates.append(update[len(update) // 2])
        elif part2 and not valid:
            valid_updates.append(update[len(update) // 2])
        # if valid:
        #     print(f"{update} valid")

        # else:
        #     print(f"{update} invalid")
    return valid_updates


get_input()

print("Part1: ", sum([int(x) for x in execute(False)]))
print("Part2: ", sum([int(x) for x in fix_invalid()]))
