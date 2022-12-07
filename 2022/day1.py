def find_max_1() -> list:
    """
    Open het bestand en creeer daar een lijst uit met
    de waardes.

    :return max: int, max calories in the file
    """
    sums = []
    with open("day1_input.txt", "r") as file:
        lines = file.read().split("\n\n")
        for line in lines:
            line = line.split("\n")
            line_sum = sum([int(i) for i in line if i != ''])
            sums.append(line_sum)

    return max(sums)


def find_max_2() -> list:
    """
    Open het bestand en creeer daar een lijst uit met
    de waardes.

    :return max: int, max calories in the file
    """
    sums = []
    with open("day1_input.txt", "r") as file:
        lines = file.read().split("\n\n")
        for line in lines:
            line = line.split("\n")
            line_sum = sum([int(i) for i in line if i != ''])
            sums.append(line_sum)
    sums = sorted(sums)[-3:]
    return sum(sums)


if __name__ == "__main__":
    print(find_max_2())
