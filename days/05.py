from get_day_input import get_input
import re


data = get_input(5)

# Not transforming all the data today as it will take more time than the puzzle.
blocks = {
    1: ["V", "C", "D", "R", "Z", "G", "B", "W"],
    2: ["G", "W", "F", "C", "B", "S", "T", "V"],
    3: ["C", "B", "S", "N", "W"],
    4: ["Q", "G", "M", "N", "J", "V", "C", "P"],
    5: ["T", "S", "L", "F", "D", "H", "B"],
    6: ["J", "V", "T", "W", "M", "N"],
    7: ["P", "F", "L", "C", "S", "T", "G"],
    8: ["B", "D", "Z"],
    9: ["M", "N", "Z", "W"],
}

commands = [re.findall(r'\d+', cmd) for cmd in data.split("\n\n")[1].splitlines()]


def one(reverse: bool = True) -> str:
    """
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    """
    for amt, frm, to in commands:
        to_move = blocks[int(frm)][-int(amt):]
        blocks[int(frm)] = blocks[int(frm)][:-int(amt)]
        if reverse:
            to_move = reversed(to_move)
        blocks[int(to)].extend(to_move)

    return "".join([stack[-1] for _, stack in blocks.items()])


def two() -> str:
    """
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    """
    return one(reverse=False)


print(f"1. {one()}")
print(f"2. {two()}")
