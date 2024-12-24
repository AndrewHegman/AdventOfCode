part1 = 0
part2 = 0


def calculate_fuel(mass):
    return (int(mass) // 3) - 2


with open("input.txt", "r") as f:
    for line in f:
        fuel = calculate_fuel(line)
        part1 += fuel

        part2 += fuel
        while fuel > 0:
            fuel = calculate_fuel(fuel)
            if fuel > 0:
                part2 += fuel


print("Part 1:", part1)
print("Part 2:", part2)
