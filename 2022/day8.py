def count_visible(trees, max_height):
    count = 0
    for tree in trees:
        count += 1
        if tree >= max_height:
            break
    return count


def get_all_visible1():
    amount = 0
    tree_grid = []
    with open("day8_input.txt", "r") as file:
        content = file.read().split("\n")
        tree_grid = [[int(y) for y in x] for x in content]

        amount += 4 * len(tree_grid) - 4 
        for row in range(1, len(tree_grid) - 1):
            for col in range(1, len(tree_grid) - 1):
                cur = tree_grid[col][row]

                vertical = [tree_grid[i][row] for i in [i for i in range(len(tree_grid))]]

                tall_left = all([tree < cur for tree in tree_grid[col][0:row]])
                tall_right = all([tree < cur for tree in tree_grid[col][row+1:len(tree_grid)]])
                tall_up = all([tree < cur for tree in vertical[0:col]])
                tall_down = all([tree < cur for tree in vertical[col+1:len(tree_grid)]])

                amount += 1 if tall_up or tall_down or tall_left or tall_right else 0

    return amount


def get_all_visible2():
    score = 0
    max_score = 0
    tree_grid = []
    with open("day8_input.txt", "r") as file:
        content = file.read().split("\n")
        tree_grid = [[int(y) for y in x] for x in content]

        for row in range(len(tree_grid)):
            for col in range(0, len(tree_grid)):
                cur = tree_grid[col][row]

                vertical = [tree_grid[i][row] for i in [i for i in range(len(tree_grid))]]

                tall_left = tree_grid[col][0:row]
                tall_right = tree_grid[col][row+1:len(tree_grid)]
                tall_up = vertical[0:col]
                tall_down = vertical[col+1:len(tree_grid)]

                score = count_visible(tall_left[::-1], cur)
                score *= count_visible(tall_right, cur)
                score *= count_visible(tall_up[::-1], cur)
                score *= count_visible(tall_down, cur)

                if score > max_score:
                    max_score = score
    return max_score


if __name__ == "__main__":
    print(get_all_visible2())
