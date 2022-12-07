def get_total_score_1():
    moves = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    scores = [3, 0, 6]

    score = 0
    with open("day2_input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            elf, you = line.replace("\n", "").split(" ")
            score += (scores[moves[elf] - moves[you]] + moves[you])
    return score


def get_total_score_2():
    outcomes = {'X': 0, 'Y': 3, 'Z': 6}
    games = [
        ['A', 'X'],  # 3
        ['A', 'Y'],  # 1
        ['A', 'Z'],  # 2
        ['B', 'X'],  # 1
        ['B', 'Y'],  # 2
        ['B', 'Z'],  # 3
        ['C', 'X'],  # 2
        ['C', 'Y'],  # 3
        ['C', 'Z'],  # 1
    ]
    scores = [3, 1, 2, 1, 2, 3, 2, 3, 1]

    score = 0
    with open("day2_input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            elf, you = line.replace("\n", "").split(" ")
            your_outcome = outcomes[you]
            elf_outcome = scores[games.index([elf, you])]
            score += your_outcome + elf_outcome
    return score


if __name__ == "__main__":
    print(get_total_score_2())
