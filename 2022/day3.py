import string


def get_total_commons_1():
    alpha = string.ascii_letters
    sum_of_letters = 0

    with open("day3_input.txt", "r") as file:
        for line in file.readlines():
            line = line.replace("\n", "")
            first, second = set(line[:len(line)//2]), set(line[len(line)//2:])
            common = first.intersection(second)
            sum_of_letters += alpha.index("".join(common)) + 1
    return sum_of_letters


def get_total_commons_2():
    alpha = string.ascii_letters
    sum_of_letters = 0

    with open("day3_input.txt", "r") as file:
        lines = file.readlines()
        lines = list(zip(*[iter(lines)]*3))
        for line in lines:
            first, second, third = line
            first = set(first.strip())
            second = set(second.strip())
            third = set(third.strip())

            sum_of_letters += alpha.index("".join(first & second & third)) + 1
    return sum_of_letters


if __name__ == "__main__":
    print(get_total_commons_2())
