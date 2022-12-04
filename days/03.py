from get_day_input import get_input


data = get_input(3).splitlines()


def char_to_int(c: str) -> int:
    """
    Converts alphabet string to integer using unicode.
    """
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38


def one() -> int:
    """
    Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those
    item types?
    """
    priorities = 0
    for rucksack in data:
        p1, p2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        common = set(p1) & set(p2)
        priorities += char_to_int(common.pop())
    return priorities


def two() -> int:
    """
    Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of
    those item types?
    """
    def chunker(seq, size: int = 3):
        """
        Chunks data in groups of three.
        """
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    priorities = 0
    for r1, r2, r3 in chunker(data):
        common = set(r1) & set(r2) & set(r3)
        priorities += char_to_int(common.pop())
    return priorities


print(f"1. {one()}")
print(f"2. {two()}")
