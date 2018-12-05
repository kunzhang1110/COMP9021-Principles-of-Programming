# Merging two strings into a third
import sys
string_1 = input("1:")
string_2 = input("2:")
string_3 = input("3:")
all_string = [string_1, string_2, string_3]
all_string_len = [len(x) for x in all_string]
longest_number = all_string_len.index(max(all_string_len)) + 1
all_string.sort(key=len)
print(all_string)

for c in all_string[2]:
    if all_string[0]:
        if c == all_string[0][0]:
            all_string[0] = all_string[0][1:]
            continue
        elif all_string[1]:
            if c == all_string[1][0]:
                all_string[1] = all_string[1][1:]
                continue
            else:
                print("No solution")
                sys.exit()
                break
print("{} can be merged by others".format(longest_number))


