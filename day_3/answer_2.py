import os
from rich import print
import collections

lines = open("input.txt", "r").readlines()


def get_score_from_letter(matching_letter):
    if matching_letter.islower():
        return ord(matching_letter) - 96

    if matching_letter.isupper():
        return ord(matching_letter) - 38


def get_matching_letter(pair_of_3):
    print(pair_of_3)
    num_1 = list(pair_of_3[0].strip("\n"))
    num_2 = list(pair_of_3[1].strip("\n"))
    num_3 = list(pair_of_3[2].strip("\n"))

    matching_letter = ""
    for letter in num_1:
        if letter in num_2 and letter in num_3:
            matching_letter = letter
            print("matching_letter: ", matching_letter)
            break
    return matching_letter


score = 0
pair_of_3 = []
for line in lines:
    pair_of_3.append(line)
    if len(pair_of_3) == 3:
        matching_letter = get_matching_letter(pair_of_3)
        score += get_score_from_letter(matching_letter)
        pair_of_3 = []


print("score: ", score)
