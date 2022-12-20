from get_day_input import get_input
from collections import defaultdict
from heapq import heappop, heappush
import math


def convert_char_to_int(c: str):
    """
    Converts character to integer based on ASCII value.
    """
    if c == "E":
        return 27  # maximum
    elif c == "S":
        return 0  # minimum
    else:
        return int(ord(c) - 96)  # 1 - 26


data = [[convert_char_to_int(c) for c in row] for row in get_input(12).splitlines()]


def get_nodes(c: int) -> list[tuple]:
    """
    Returns the start node (c=0) and the end_node (c=27). Can also return multiple start nodes (c=1).
    """
    return [(sub.index(c), i) for (i, sub) in enumerate(data) if c in sub]


def calculate_fewest_steps(part2_node: tuple = None) -> int:
    """
    Use the A* search algorithm to retrieve the shortest path and associated shortest path (with priority queue).
    (Copied from AOC 2021 day 15).
    """

    def is_valid_node(x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        Check whether the proposed node is valid.
        """
        is_on_map = min_x <= x2 <= max_x and min_y <= y2 <= max_y
        if is_on_map:
            return data[y1][x1] + 1 >= data[y2][x2]
        else:
            return False

    min_x = min_y = 0
    max_y = len(data) - 1
    max_x = len(data[0]) - 1

    start_node = get_nodes(0)[0] if not part2_node else part2_node
    end_node = get_nodes(27)[0]
    risk_dict = defaultdict(lambda: math.inf)
    risk_dict[start_node] = 0

    open_list = []
    heappush(open_list, (0, start_node))

    unvisited = {(x, y) for x in range(max_x + 1) for y in range(max_y + 1)}

    # Loop until the end node has been found.
    while end_node in unvisited:
        current_risk, current = heappop(open_list)

        # Double check.
        if current not in unvisited:
            continue

        child_nodes = []
        for x_pos_change, y_pos_change in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # left, right, down, up.

            x, y = current

            # New node positions.
            x_pos = x + x_pos_change
            y_pos = y + y_pos_change

            # Append new node to child nodes if it is valid.
            if is_valid_node(x, y, x_pos, y_pos):
                child_nodes.append((x_pos, y_pos))

        for child_node in child_nodes:

            # Only consider child nodes not in closed list.
            if child_node not in unvisited:
                continue

            # Only update (cumulative) risk only if it is lower.
            child_risk = min(
                risk_dict[child_node],
                risk_dict[current] + 1,
            )

            risk_dict[child_node] = child_risk
            heappush(open_list, (child_risk, child_node))

        unvisited.remove(current)

    return int(risk_dict[end_node])


def one() -> int:
    """
    What is the fewest steps required to move from your current position to the location that should get the best
    signal?
    """
    return calculate_fewest_steps()


def two() -> int:
    """
    What is the fewest steps required to move starting from any square with elevation a to the location that should get
    the best signal?
    """
    min_steps = math.inf
    start_nodes = get_nodes(1)
    for node in start_nodes:
        steps = calculate_fewest_steps(part2_node=node)
        min_steps = min(steps, min_steps)
    return min_steps


print(f"1. {one()}")
print(f"2. {two()}")
