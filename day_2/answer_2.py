lines = open("input.txt", "r").readlines()

first_score = {"Rock": 1, "Paper": 2, "Scissors": 3}
second_score = {"Lose": 0, "Draw": 3, "Win": 6}

player_a = {"A": "Rock", "B": "Paper", "C": "Scissors"}
player_b = {"X": "Lose", "Y": "Draw", "Z": "Win"}

score = 0
for line in lines:
    player_a_choice, result = list(line)[0], list(line)[2]
    player_a_choice, result = player_a[player_a_choice], player_b[result]
    print("player_a_choice: ", player_a_choice, "result", result)

    player_b_choice = ""

    if result == "Win":
        if player_a_choice == "Rock":
            player_b_choice = "Paper"
        if player_a_choice == "Paper":
            player_b_choice = "Scissors"
        if player_a_choice == "Scissors":
            player_b_choice = "Rock"

    if result == "Lose":
        if player_a_choice == "Paper":
            player_b_choice = "Rock"
        if player_a_choice == "Scissors":
            player_b_choice = "Paper"
        if player_a_choice == "Rock":
            player_b_choice = "Scissors"

    if result == "Draw":
        player_b_choice = player_a_choice

    score += second_score[result]
    score += first_score[player_b_choice]


print("score: ", score)
