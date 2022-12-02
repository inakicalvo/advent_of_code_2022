file = "input.txt"


def get_max_cals(input):
    # Read file and create list splitting by double line breaks
    with open(input) as file:
        elf_list = file.read().split("\n\n")

    # Find and print max calories
    elf_calories = []
    for elf in elf_list:
        calories = sum(map(int, elf.splitlines()))
        elf_calories.append(calories)
    print("The elf carrying the most calories carries",
          max(elf_calories), "cals.")

    # Sum the cals of the 3 top loads
    sorted_cals = sorted(elf_calories)
    print("And the result of summing the calories of the three elves with the most calorie rich loads is", sum(
        sorted_cals[-3:]), ".")


get_max_cals(file)
