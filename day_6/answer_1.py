def get_marker(line):
    length = len(line)
    for i in range(length):
        string_set = line[i : 4 + i]

        check = len(set(string_set))
        print(string_set, check, i)
        if check == 4:
            print("letters are unique!")
            break

    answer = i + 4
    print(answer)
    return answer


lines = open("input.txt", "r").readlines()
for line in lines:
    print(get_marker(line))
