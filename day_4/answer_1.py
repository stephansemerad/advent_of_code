lines = open("input.txt", "r").readlines()

example_lines = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]


def convert_to_range(group):
    section_1, section_2 = group.split("-")
    group_range = list(range(int(section_1), int(section_2) + 1))
    return list(set(group_range))


score = 0
for line in lines:
    group_1, group_2 = line.split(",")
    group_1, group_2 = convert_to_range(group_1), convert_to_range(group_2)
    comparison = list(set(group_1).intersection(set(group_2)))
    print(group_1, group_2, comparison)

    if comparison == group_1 or comparison == group_2:
        print("one_score")
        score += 1

    # print("")

print("score: ", score)
