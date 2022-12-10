from get_day_input import get_input


data = [[int(tree) for tree in line] for line in get_input(8).splitlines()]


def can_be_seen(tree: tuple[int, int], height: int) -> bool:
    """
    Returns whether a tree can be seen from an outside perspective.
    """
    def min_surrounding_tree() -> int:
        """
        Get minimum height of maximum trees surrounding the current tree (x, y).
        """
        left = data[y][:x]
        right = data[y][x+1:]
        up = [row[x] for row in data[:y]]
        down = [row[x] for row in data[y+1:]]
        return min(
            max(left),
            max(right),
            max(up),
            max(down)
        )

    y_min, y_max = 0, len(data) - 1
    x_min, x_max = 0, len(data[0]) - 1
    x, y = tree

    if x in [x_min, x_max] or y in [y_min, y_max]:
        return True
    elif height > min_surrounding_tree():
        return True
    else:
        return False


def one() -> int:
    """
    Consider your map; how many trees are visible from outside the grid?
    """
    tree_set = set()
    for y, col in enumerate(data):
        for x, height in enumerate(col):
            tree = (x, y)
            if can_be_seen(tree=tree, height=height):
                tree_set.add(tree)

    return len(tree_set)


def scenic_score(tree: tuple[int, int], height: int) -> int:
    """
    Multiplication of viewing distance in all four directions.
    """

    def scan(trees: list[int]) -> int:
        """
        Scan in a specific direction and count the number of trees out of view.
        """
        count = 0
        for t in trees:
            count += 1
            if height <= t:
                break
        return count

    x, y = tree
    left = data[y][:x][::-1]
    right = data[y][x+1:]
    up = [row[x] for row in data[:y]][::-1]
    down = [row[x] for row in data[y+1:]]

    return scan(left) * scan(right) * scan(up) * scan(down)


def two() -> int:
    """
    Consider each tree on your map. What is the highest scenic score possible for any tree?
    """
    scores = set()
    for y, col in enumerate(data):
        for x, height in enumerate(col):
            tree = (x, y)
            scores.add(scenic_score(tree=tree, height=height))

    return max(scores)


print(f"1. {one()}")
print(f"2. {two()}")
