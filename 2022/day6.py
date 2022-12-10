def get_indexes1():
    indexes = []
    with open("day6_input.txt", "r") as file:
        content = file.read()
        parts = [content[i:i+4] for i in range(len(content) - 4 + 1)]
        for i, part in enumerate(parts):
            if len(set(part)) == len(part):
                indexes.append(i+4)
    return indexes[0]


def get_indexes2():
    indexes = []
    with open("day6_input.txt", "r") as file:
        content = file.read()
        parts = [content[i:i+14] for i in range(len(content) - 14 + 1)]
        for i, part in enumerate(parts):
            if len(set(part)) == len(part):
                indexes.append(i+14)
    return indexes[0]


if __name__ == "__main__":
    print(get_indexes2())





    # indexes = []
    # test_str = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    # parts = [test_str[i:i+4] for i in range(len(test_str) - 4 + 1)]
    # for i, part in enumerate(parts):
    #     if len(set(part)) == len(part):
    #         indexes.append(i + 4)
    # print(indexes[0])
