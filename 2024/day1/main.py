import sys

col1 = []
col2 = []
diff = 0
simmilarity_score = 0

with open(
    "test.txt" if len(sys.argv) > 1 and sys.argv[1] == "--test" else "input.txt", "r"
) as f:
    for line in f:
        col1.append(int(line.split()[0].strip()))
        col2.append(int(line.split()[1].strip()))

    col1.sort()
    col2.sort()

    for i in range(len(col1)):
        diff += abs(col1[i] - col2[i])
        simmilarity_score += col1[i] * col2.count(col1[i])

print("Part 1: ", diff)
print("Part 2: ", simmilarity_score)
