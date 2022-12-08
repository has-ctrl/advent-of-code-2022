from get_day_input import get_input


data = get_input(7).splitlines()


def one(part2: bool = False) -> int:
    """
    Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those
    directories?
    """
    max_size = 100000
    loc = []
    dir_size = {}
    for line in data:
        match line.split():
            case "$", "cd", "/":  # Escape root.
                loc = ["/"]
            case "$", "cd", "..":  # Move down.
                loc.pop()
            case "$", "cd", x:  # Move up.
                loc.append(f"{x}/")
            case "$", _:  # List files/dirs.
                pass
            case "dir", _:  # Skip unopened dir.
                pass
            case n, _:  # File size.
                root = loc.copy()
                while root:
                    if dir_size.get(tuple(root)):
                        dir_size[tuple(root)] += int(n)
                    else:
                        dir_size[tuple(root)] = int(n)
                    root.pop()

    if not part2:
        return sum([v for v in dir_size.values() if v <= max_size])
    else:
        return min([v for v in dir_size.values() if v >= dir_size[tuple(["/"])] - 40_000_000])


def two() -> int:
    """
    Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.
    What is the total size of that directory?
    """
    return one(part2=True)


print(f"1. {one()}")
print(f"2. {two()}")
