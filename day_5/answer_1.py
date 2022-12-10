"""
                    [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9 
"""
from rich import print

stacks = [
    ["C", "Q", "B"],
    ["Z", "W", "Q", "R"],
    ["V", "L", "R", "M", "B"],
    ["W", "T", "V", "H", "Z", "C"],
    ["G", "V", "N", "B", "H", "Z", "D"],
    ["Q", "V", "F", "J", "C", "P", "N", "H"],
    ["S", "Z", "W", "R", "T", "G", "D"],
    ["P", "Z", "W", "B", "N", "M", "G", "C"],
    ["P", "F", "Q", "W", "M", "B", "J", "N"],
]

lines = open("input.txt", "r").readlines()
for i in lines:
    print("---------------------------------")
    print("before: ")
    print(stacks)
    print(i)
    i = i.split(" ")
    _amount, _from, _to = i[1], i[3], i[5]
    moving = stacks[int(_from) - 1][0 : int(_amount)]
    del stacks[int(_from) - 1][0 : int(_amount)]
    moving.reverse()
    stacks[int(_to) - 1] = moving + stacks[int(_to) - 1]

    print("moving: ", moving)
    if len(moving) < 1:
        break
    print(stacks)
    print("")

print(stacks)
answer = []
for i in range(len(stacks)):
    answer += stacks[i][:1]

answer = "".join(answer)
print("answer: ", answer)

# TNSCVHMHV
