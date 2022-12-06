from get_day_input import get_input
import re


data = get_input(4).splitlines()


def one() -> int:
    """
    In how many assignment pairs does one range fully contain the other?
    """
    count = 0
    for pairs in data:
        p1s1, p1s2, p2s1, p2s2 = re.findall(r'\d+', pairs)
        p1, p2 = set(range(int(p1s1), int(p1s2)+1)), set(range(int(p2s1), int(p2s2)+1))
        if p1.issuperset(p2) or p1.issubset(p2):
            count += 1
    return count


def two() -> int:
    """
    In how many assignment pairs do the ranges overlap?
    """
    count = 0
    for pairs in data:
        p1s1, p1s2, p2s1, p2s2 = re.findall(r'\d+', pairs)
        p1, p2 = set(range(int(p1s1), int(p1s2)+1)), set(range(int(p2s1), int(p2s2)+1))
        if p1.intersection(p2):
            count += 1
    return count


print(f"1. {one()}")
print(f"2. {two()}")
