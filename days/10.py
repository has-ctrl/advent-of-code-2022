from get_day_input import get_input


data = get_input(10).splitlines()


def one(part2: bool = False) -> int | dict:
    """
    Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six
    signal strengths?
    """
    special_cycle = 20
    signal_strength = 0
    cycle = 0
    x = 1
    cycle_dict = {cycle+1: x}
    for cmd in data:
        to_add = 0

        if cmd == "noop":
            cycle += 1
        else:
            to_add = int(cmd.split()[1])
            cycle += 2

        if cycle >= special_cycle:
            signal_strength += special_cycle * x
            special_cycle += 40

        x += to_add
        cycle_dict[cycle] = x

    if not part2:
        return signal_strength
    else:
        return cycle_dict | {c: cycle_dict[c-1] for c in range(1, cycle + 1) if c not in cycle_dict}


def two() -> str:
    """
    Render the image given by your program. What eight capital letters appear on your CRT?
    """
    complete_dict = one(part2=True)
    adj_x = 0
    to_print = "#"
    for x in range(1, max(complete_dict.keys())+1):
        if x % 40 == 0:
            print(f"{to_print}")
            to_print = ""
            adj_x += 40

        sprite_pos = [complete_dict[x] + n for n in range(-1, 2)]
        to_print += "#" if x - adj_x in sprite_pos else "."

    return "See above!"


print(f"1. {one()}\n")
print(f"\n2. {two()}")
