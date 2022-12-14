def get_total():
    total = 0
    x = 1
    cycle = 1

    with open("day10_input.txt", "r") as file:
        for line in file.readlines():
            if (cycle % 40) == 20:
                total += cycle * x
            if line.rstrip() == "noop":
                cycle += 1
            else:
                value = int(line.split()[1])
                if ((cycle + 1) % 40) == 20:
                    total += (cycle + 1) * x
                cycle += 2
                x += value

        if (cycle % 40) == 20:
            total += cycle * x
    return total


def get_letter():
    cycle = 0
    x = 1

    bits = [1] * 241

    with open("day10_input.txt", "r") as file:
        for line in file.readlines():
            if line.rstrip() == "noop":
                cycle += 1
                bits[cycle] = x
            else:
                value = int(line.split()[1])
                bits[cycle + 1] = x
                x += value

                cycle += 2
                bits[cycle] = x

    answer = [[None] * 40 for _ in range(6)]

    for row in range(6):
        for col in range(40):
            counter = row * 40 + col + 1
            if abs(bits[counter - 1] - (col)) <= 1:
                answer[row][col] = "##"
            else:
                answer[row][col] = ".."
    for row in answer:
        print("".join(row))


if __name__ == "__main__":
    print(get_total())
    get_letter()
