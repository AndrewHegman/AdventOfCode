import itertools

valid = 0
part1_ops = ["*", "+"]
part2_ops = ["*", "+", "||"]


def evaluate(nums, ops):
    s = nums[0]
    for x in range(len(ops)):
        if ops[x] == "+":
            s += nums[x + 1]
        elif ops[x] == "*":
            s *= nums[x + 1]
        else:
            s = int(str(s) + str(nums[x + 1]))
    return s


with open("input.txt") as f:
    lines = [x.strip().split(":") for x in f.readlines()]
    for x in lines:
        ans = x[0]
        nums = [int(y) for y in x[1].lstrip().split(" ")]
        # print(len(nums))
        for op in [y for y in itertools.product(part2_ops, repeat=len(nums) - 1)]:
            # print(op)
            _ans = evaluate(nums, op)
            if _ans == int(ans):
                valid += int(ans)
                break


print("Answer: ", valid)
