from get_day_input import get_input

data = get_input(9).splitlines()


def close(head_x: int, head_y: int, tail_x: int, tail_y: int) -> bool:
    """
    Check if the tail is still close enough to the head.
    """
    return abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1


def one() -> int:
    """
    Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least
    once?
    """
    head_x = tail_x = 0
    head_y = tail_y = 0
    visited = {(tail_x, tail_y)}

    for motion in data:

        match motion.split():
            case "L", step:
                for _ in range(int(step)):
                    prev_head_x, prev_head_y = head_x, head_y

                    head_x -= 1
                    if not close(head_x, head_y, tail_x, tail_y):
                        tail_x, tail_y = prev_head_x, prev_head_y
                        visited.add((tail_x, tail_y))
            case "R", step:
                for _ in range(int(step)):
                    prev_head_x, prev_head_y = head_x, head_y

                    head_x += 1
                    if not close(head_x, head_y, tail_x, tail_y):
                        tail_x, tail_y = prev_head_x, prev_head_y
                        visited.add((tail_x, tail_y))
            case "U", step:
                for _ in range(int(step)):
                    prev_head_x, prev_head_y = head_x, head_y

                    head_y -= 1
                    if not close(head_x, head_y, tail_x, tail_y):
                        tail_x, tail_y = prev_head_x, prev_head_y
                        visited.add((tail_x, tail_y))
            case "D", step:
                for _ in range(int(step)):
                    prev_head_x, prev_head_y = head_x, head_y

                    head_y += 1
                    if not close(head_x, head_y, tail_x, tail_y):
                        tail_x, tail_y = prev_head_x, prev_head_y
                        visited.add((tail_x, tail_y))
    return len(visited)


def two() -> int:
    """
    Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the
    rope visit at least once?
    """
    def follow(h_x: int, h_y: int, t_x: int, t_y: int) -> tuple[int, int]:
        """
        Given location of head (or different tail) move tail to correct coordinate.
        """
        if close(h_x, h_y, t_x, t_y):
            return t_x, t_y

        if h_x == t_x:  # Same x-axis.
            if h_y < t_y:
                return t_x, t_y - 1
            else:
                return t_x, t_y + 1
        elif h_y == t_y:  # Same y-axis.
            if h_x < t_x:
                return t_x - 1, t_y
            else:
                return t_x + 1, t_y
        else:  # Diagonal
            diff_x = -1 if h_x < t_x else +1
            diff_y = -1 if h_y < t_y else +1
            return t_x + diff_x, t_y + diff_y

    n_knots = 10
    rope = [(0, 0)] * n_knots
    visited = {rope[n_knots-1]}
    for motion in data:
        d, step = motion.split()
        for _ in range(int(step)):
            head_x, head_y = rope[0]
            if d == "L":
                head_x -= 1
            elif d == "R":
                head_x += 1
            elif d == "U":
                head_y -= 1
            else:
                head_y += 1

            rope[0] = (head_x, head_y)
            for i, (knot_x, knot_y) in enumerate(rope[1:]):
                new_x, new_y = follow(h_x=rope[i][0], h_y=rope[i][1], t_x=knot_x, t_y=knot_y)
                if (knot_x, knot_y) == (new_x, new_y):  # no change
                    break
                elif i == n_knots - 2:
                    visited.add((new_x, new_y))
                rope[i+1] = new_x, new_y

    return len(visited)


print(f"1. {one()}")
print(f"2. {two()}")
