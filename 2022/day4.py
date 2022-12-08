from itertools import chain


def get_amount1():
    amount = 0

    with open("day4_input.txt", "r") as file:
        for line in file.readlines():
            line = line.strip()
            a, b, c, d = list(chain(*[x.split("-") for x in line.split(",")]))
            amount += 1 if 0 >= (int(a)-int(c))*(int(b)-int(d)) else 0

    return amount


def get_amount2():
    amount = 0

    with open("day4_input.txt", "r") as file:
        for line in file.readlines():
            line = line.strip()
            a, b, c, d = list(chain(*[x.split("-") for x in line.split(",")]))
            amount += 1 if 0 >= (int(a)-int(d))*(int(b)-int(c)) else 0

    return amount


if __name__ == "__main__":
    print(get_amount2())
