def make_directory_tree():
    dirs = {}
    pwd = []
    with open("day7_input.txt", "r") as file:
        content = file.read().split("\n")
        lines = [x.split(" ") for x in content]
        for line in lines:
            if line[0] == "$" and line[1] == "cd":
                if line[2] == "/":
                    pwd = ['//']
                    dirs['//'] = 0
                elif line[2] == "..":
                    pwd.pop()
                else:
                    current_dir = "/".join(pwd) + "/" + line[2]
                    pwd.append(current_dir)
                    if not dirs.get(current_dir):
                        dirs[current_dir] = 0
            elif line[0].isnumeric():
                for d in pwd:
                    dirs[d] += int(line[0])
    return dirs


def get_large_files1(dirs: dict):
    large_files = []
    for x in dirs.values():
        if x <= 100_000:
            large_files.append(x)
    return sum(large_files)


def get_large_files2(dirs: dict):
    large_files = []
    space_needed = dirs['//'] - 40_000_000
    for x in dirs.values():
        if x > space_needed:
            large_files.append(x)
    return min(large_files)


if __name__ == "__main__":
    dirs = make_directory_tree()
    print(get_large_files1(dirs))
    print(get_large_files2(dirs))
