from get_day_input import get_input


data = get_input(day=2).splitlines()

SHAPES = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

OUTCOMES = {
    "loss": 0,
    "draw": 3,
    "win": 6,
}


def calc_score(shape1: str, shape2: str) -> int:
    """
    Returns whether shape1 wins from shape2 in a match-up.
    """
    res = SHAPES.get(shape2)
    if shape1 == "A":  # Rock
        if shape2 == "X":
            res += OUTCOMES.get("draw")
        elif shape2 == "Y":
            res += OUTCOMES.get("win")
        else:
            res += OUTCOMES.get("loss")
    elif shape1 == "B":  # Paper
        if shape2 == "Y":
            res += OUTCOMES.get("draw")
        elif shape2 == "Z":
            res += OUTCOMES.get("win")
        else:
            res += OUTCOMES.get("loss")
    else:  # Scissors
        if shape2 == "Z":
            res += OUTCOMES.get("draw")
        elif shape2 == "X":
            res += OUTCOMES.get("win")
        else:
            res += OUTCOMES.get("loss")
    return res


def one() -> int:
    """
    What would your total score be if everything goes exactly according to your strategy guide?
    """
    score = 0
    for game in data:
        p1, p2 = game.split()
        score += calc_score(p1, p2)
    return score


def calc_new_score(shape1: str, strategy: str) -> int:
    """
    Returns the score when you apply the strategy when opponent plays shape1.
    """
    if strategy == "X":  # lose
        if shape1 == "A":
            return calc_score(shape1, "Z")
        elif shape1 == "B":
            return calc_score(shape1, "X")
        else:
            return calc_score(shape1, "Y")
    elif strategy == "Y":  # draw
        if shape1 == "A":
            return calc_score(shape1, "X")
        elif shape1 == "B":
            return calc_score(shape1, "Y")
        else:
            return calc_score(shape1, "Z")
    else:  # win
        if shape1 == "A":
            return calc_score(shape1, "Y")
        elif shape1 == "B":
            return calc_score(shape1, "Z")
        else:
            return calc_score(shape1, "X")


def two() -> int:
    """
    Following the Elf's instructions for the second column, what would your total score be if everything goes exactly
    according to your strategy guide?
    """
    score = 0
    for game in data:
        p1, strategy = game.split()
        score += calc_new_score(p1, strategy)

    return score


print(f"1. {one()}")
print(f"2. {two()}")
