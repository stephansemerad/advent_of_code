

import os
from rich import print

elves = {}
lines = open('input.txt', 'r').readlines()
count = 1
for line in lines:
    value = line.strip('\n').strip('\r')
    value = 0 if value == '' else int(value)

    if value == 0:
        count += 1
    elves[f'{count}'] = elves[f'{count}']+ value if f'{count}' in elves else value

elves = sorted(elves.items(), key=lambda x: x[1], reverse=True)
print(elves[0][1])
