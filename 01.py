from get_day_input import get_input


data = get_input(day=1).splitlines()


def one() -> int:
    """
    Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    """
    count = 0
    max_count = 0
    for cals in data:
        if cals:
            count += int(cals)
            continue
        elif count > max_count:
            max_count = count
        count = 0

    return max_count


def two() -> int:
    """
    Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    """
    count = 0
    calories = set()
    for cals in data:
        if cals:
            count += int(cals)
            continue
        calories.add(count)
        count = 0

    return sum(sorted(calories, reverse=True)[:3])


print(f"1. {one()}")
print(f"2. {two()}")
