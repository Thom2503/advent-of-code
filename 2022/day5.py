from collections import defaultdict


def get_last_letters1():
    with open("day5_input.txt", "r") as file:
        stacks = defaultdict(list)
        for line in file.readlines():
            if "[" in line:
                for i, c in enumerate(line):
                    if c.isalpha():
                        stacks[i//4 + 1].insert(0, c)
            else:
                l = line.split()
                if len(l) == 6:
                    amount, fr, to = int(l[1]), int(l[3]), int(l[5])
                    move = stacks[fr][-amount:]
                    stacks[fr] = stacks[fr][:-amount]
                    stacks[to] = stacks[to] + move[::-1]
    return "".join(l[-1] for i, l in sorted(stacks.items()))


def get_last_letters2():
    with open("day5_input.txt", "r") as file:
        stacks = defaultdict(list)
        for line in file.readlines():
            if "[" in line:
                for i, c in enumerate(line):
                    if c.isalpha():
                        stacks[i//4 + 1].insert(0, c)
            else:
                l = line.split()
                if len(l) == 6:
                    amount, fr, to = int(l[1]), int(l[3]), int(l[5])
                    move = stacks[fr][-amount:]
                    stacks[fr] = stacks[fr][:-amount]
                    stacks[to] = stacks[to] + move
    return "".join(l[-1] for i, l in sorted(stacks.items()))


if __name__ == "__main__":
    print(get_last_letters2())












    # for line in lines[0].split("\n"):
    #     if line.strip() == "":
    #         break
    #     for i, c in enumerate(line):
    #         if c.isalpha():
    #             stacks[i//4].append(c)
    #     line = ""
    # for line in lines[1].split("\n"):
    #     if len(line) == 6:
    #         amount, fr, to = [x for x in line.split(" ") if x.isnumeric()]
    #         from_stack = stacks[int(fr) - 1]

    #         vals = from_stack[:int(amount)]
    #         for x in vals:
    #             stacks[int(to) - 1].append(x)

    #         from_stack = [x for x in from_stack if x not in vals]
    # print(stacks)
