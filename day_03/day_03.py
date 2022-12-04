input = "day_03/day_03.txt"


def fix_backpacks(input):
    all_backpacks = []
    # Read file
    with open(input) as file:
        backpacks = file.read().splitlines()

    priority_score = 0
    priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for backpack in backpacks:
        # Get elements in each compartiment
        first_comp = backpack[:int(len(backpack) / 2)]
        second_comp = backpack[int(len(backpack) / 2):]

        # Find items repeated in the two compartiments
        char = [item for item in first_comp if item in second_comp][0]

        # Update priority_score adding points for each repeated item
        priority_score += priority.rfind(char) + 1

    print("The sum of the priorities is", priority_score)

    # Second part
    groups = []
    priority_score = 0

    # Make groups with three elves per group
    for i in range(0, len(backpacks), 3):
        groups.append(backpacks[i:i + 3])

    # Find items in common among the 3 members of each group
    items_in_common = []

    for group in groups:
        common_item = list(set.intersection(*map(set, group)))
        items_in_common.append(common_item)
    items_in_common = [item for sublist in items_in_common for item in sublist]
    print(items_in_common)

    for item in items_in_common:
        priority_score += priority.rfind(item) + 1

    print(priority_score)


fix_backpacks(input)
