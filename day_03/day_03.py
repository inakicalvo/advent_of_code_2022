input = "day_03/day_03.txt"


def fix_backpacks(input):
    all_backpacks = []
    # Read file
    with open(input) as file:
        backpacks = file.readlines()

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


fix_backpacks(input)
