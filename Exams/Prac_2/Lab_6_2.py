#  merging two strings
string_1 = "ab"
string_2 = "cd"
string_3 = "adcb"

all_strings = [string_1, string_2, string_3]
display_rank = ["first", "second", "third"]
all_strings_copy = all_strings.copy()
all_strings_copy.sort(key=len)

def test(all_strings_copy):
    for c in all_strings_copy[2]:
        if all_strings_copy[0] and c == all_strings_copy[0][0]:
            all_strings_copy[0] = all_strings_copy[0][1:]
            continue
        elif all_strings_copy[1] and c == all_strings_copy[1][0]:
            all_strings_copy[1] = all_strings_copy[1][1:]
            continue
        else:
            return False
    if all_strings_copy[0] or all_strings_copy[1]:
        return False
    return True

if test(all_strings_copy):
    print('{} can be merged'.format(display_rank[all_strings.index(all_strings_copy[-1])]))