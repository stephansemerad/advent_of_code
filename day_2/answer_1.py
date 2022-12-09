lines = open('input.txt', 'r').readlines()

first_score = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
second_score = {'Lost': 0, 'Draw': 3, 'Won': 6}

player_a = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
player_b = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

score = 0
for line in lines:

    player_a_choice, player_b_choice= list(line)[0], list(line)[2]

    player_a_choice , player_b_choice= player_a[player_a_choice], player_b[player_b_choice]

    if player_a_choice == player_b_choice: score += second_score['Draw'];print(player_a_choice, " ", player_b_choice, ' Draw')

    if player_a_choice =='Rock' and player_b_choice == 'Paper':score += second_score['Won'];print(player_a_choice, " ", player_b_choice, ' Won')
    if player_a_choice =='Rock' and player_b_choice == 'Scissors':score += second_score['Lost'];print(player_a_choice, " ", player_b_choice, ' Lost')

    if player_a_choice =='Paper' and player_b_choice == 'Rock':score += second_score['Lost'];print(player_a_choice, " ", player_b_choice, ' Lost')
    if player_a_choice =='Paper' and player_b_choice == 'Scissors':score += second_score['Won'];print(player_a_choice, " ", player_b_choice, ' Won')

    if player_a_choice =='Scissors' and player_b_choice == 'Rock':score += second_score['Won'];print(player_a_choice, " ", player_b_choice, ' Won')
    if player_a_choice =='Scissors' and player_b_choice == 'Paper':score += second_score['Lost'];print(player_a_choice, " ", player_b_choice, ' Lost')


    score += first_score[player_b_choice]

print('score: ', score)