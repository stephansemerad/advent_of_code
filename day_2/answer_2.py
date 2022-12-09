lines = open('input.txt', 'r').readlines()

first_score = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
second_score = {'Lose': 0, 'Draw': 3, 'Win': 6}

player_a = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
player_b = {'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}

score = 0
for line in lines:
    player_a_choice, result= list(line)[0], list(line)[2]
    player_a_choice, result= player_a[player_a_choice], player_b[result]
    print('player_a_choice: ', player_a_choice, 'result', result)

    if result == 'Draw':
        player_b_choice = player_a_choice
        score = first_score['player_b_choice']
        print('player_b_choice is {player_a_choice}')


    if result == 'Win':
        if player_a_choice == 'Rock':
        if player_a_choice == 'Paper':
        if player_a_choice == 'Scissors':




#     result = player_b[player_b_choice]
#     print('result: ', result, ' player_a_choice: ', player_a_choice)



# print('score: ', score)