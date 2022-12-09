import os
from rich import print

elves = {}
lines = open("input.txt", "r").readlines()

score = 0
for line in lines:
    letter_list = list(line)
    half = int(len(letter_list) / 2)

    compartment_1 = letter_list[:half]
    compartment_2 = letter_list[half:]

    matching_letter = ""
    for i in compartment_1:
        if i in compartment_2:
            matching_letter = i
            break

    def check_letter(matching_letter):
        if matching_letter.islower():
            return ord(matching_letter) - 96

        if matching_letter.isupper():
            return ord(matching_letter) - 38

    score += check_letter(matching_letter)


print("score: ", score)
