input = "day_o2\day_02.txt"


def get_my_score(input):
    new_round_list = []
    my_score = 0
    win = 6
    draw = 3
    loss = 0
    rock = 1
    paper = 2
    scissors = 3

    # Read file
    with open(input) as file:
        round_list = file.read().split("\n")
        # Create list for each line
        for item in round_list:
            new_round_list.append(item.split(" "))

    # PART 1: Get my score for each round
    for round in new_round_list:
        if (round[0] == 'A' and round[1] == 'X'):
            my_score += draw + rock
        elif (round[0] == 'A' and round[1] == 'Y'):
            my_score += win + paper
        elif (round[0] == 'A' and round[1] == 'Z'):
            my_score += loss + scissors
        elif (round[0] == 'B' and round[1] == 'X'):
            my_score += loss + rock
        elif (round[0] == 'B' and round[1] == 'Y'):
            my_score += draw + paper
        elif (round[0] == 'B' and round[1] == 'Z'):
            my_score += win + scissors
        elif (round[0] == 'C' and round[1] == 'X'):
            my_score += win + rock
        elif (round[0] == 'C' and round[1] == 'Y'):
            my_score += loss + paper
        elif (round[0] == 'C' and round[1] == 'Z'):
            my_score += draw + scissors
    print("My score for the first exercise would be:", my_score)

    # PART 2: Get my score according to the new instructions
    my_score = 0
    for round in new_round_list:
        if (round[0] == 'A' and round[1] == 'X'):
            my_score += loss + scissors
        elif (round[0] == 'A' and round[1] == 'Y'):
            my_score += draw + rock
        elif (round[0] == 'A' and round[1] == 'Z'):
            my_score += win + paper
        elif (round[0] == 'B' and round[1] == 'X'):
            my_score += loss + rock
        elif (round[0] == 'B' and round[1] == 'Y'):
            my_score += draw + paper
        elif (round[0] == 'B' and round[1] == 'Z'):
            my_score += win + scissors
        elif (round[0] == 'C' and round[1] == 'X'):
            my_score += loss + paper
        elif (round[0] == 'C' and round[1] == 'Y'):
            my_score += draw + scissors
        elif (round[0] == 'C' and round[1] == 'Z'):
            my_score += win + rock
    print("My score for the second exercise would be:", my_score)


get_my_score(input)
