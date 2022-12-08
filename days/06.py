from get_day_input import get_input

data = get_input(6)


def one(window: int = 4) -> int:
    """
    How many characters need to be processed before the first start-of-packet marker is detected?
    """
    count = window
    for i in range(len(data) - window + 1):
        chunk = data[i:i + window]
        if len(set(chunk)) == window:
            break
        count += 1

    return count


def two() -> int:
    """
    How many characters need to be processed before the first start-of-message marker is detected?
    """
    return one(14)


print(f"1. {one()}")
print(f"2. {two()}")
