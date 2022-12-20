from get_day_input import get_input
from dataclasses import dataclass, field
import math

raw_data = [m.split("\n") for m in get_input(11).split("\n\n")]


@dataclass
class Monkey:
    n: int
    items: field(default_factory=list) = None
    val_1: str = None
    val_2: str = None
    operator: str = None
    divisible_by: int = None
    if_true: int = None
    if_false: int = None
    inspection_count: int = 0


def create_monkeys(data: list[list[str]]) -> list[Monkey]:
    """
    Initialise all the monkeys based on the input.
    """
    monkey_list = []
    for n, raw_monkey in enumerate(data):
        monkey = Monkey(n)
        for line in raw_monkey:
            match line.lstrip().split(":"):
                case "Starting items", items:
                    monkey.items = [int(i) for i in items.split(",")]
                case "Operation", operation:
                    _, val = operation.split("=")
                    val_1, op, val_2 = val.split()
                    monkey.val_1 = val_1
                    monkey.val_2 = val_2
                    monkey.operator = op
                case "Test", divisible_by:
                    monkey.divisible_by = int(divisible_by.split()[2])
                case "If true", if_true:
                    monkey.if_true = int(if_true.split()[3])
                case "If false", if_false:
                    monkey.if_false = int(if_false.split()[3])

        monkey_list.append(monkey)
    return monkey_list


def calc_lcm(monkeys: list[Monkey]) -> int:
    """
    To prevent the worry score from growing too big, we should use the least common multiple (LCM).
    """
    return math.lcm(*[monkey.divisible_by for monkey in monkeys])


def one(part2: bool = False) -> int:
    """
    Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of
    monkey business after 20 rounds of stuff-slinging simian shenanigans?
    """
    n_rounds = 20 if not part2 else 10_000
    monkeys = create_monkeys(raw_data)
    lcm = None if not part2 else calc_lcm(monkeys)

    for r in range(n_rounds):
        for monkey in monkeys:
            monkey.inspection_count += len(monkey.items)
            for item in monkey.items:
                worry_level = item if monkey.val_1 == "old" else int(monkey.val_1)
                if monkey.operator == "+":
                    worry_level += item if monkey.val_2 == "old" else int(monkey.val_2)
                else:
                    worry_level *= item if monkey.val_2 == "old" else int(monkey.val_2)
                bored_level = worry_level // 3 if not part2 else worry_level
                if lcm:
                    bored_level %= lcm
                n_monkey = monkey.if_true if bored_level % monkey.divisible_by == 0 else monkey.if_false
                monkeys[n_monkey].items.append(bored_level)
            monkey.items.clear()

    inspections = sorted([monkey.inspection_count for monkey in monkeys], reverse=True)
    return inspections[0] * inspections[1]


def two() -> int:
    """
    Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?
    """
    return one(part2=True)


print(f"1. {one()}")
print(f"2. {two()}")
