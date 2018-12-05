import sys
def solve(input_1, input_2, input_3):
    print(input_1, input_2, input_3)
    if not input_1:
        if not input_2 and not input_3:
            return True
        else:
            return False
    if input_2 and input_1[0] == input_2[0]:
        return solve(input_1[1:], input_2[1:], input_3)
    elif input_3 and input_1[0] == input_3[0]:
        return solve(input_1[1:], input_2, input_3[1:])
    else:
        return False

input_1 = "aaaaa"
input_2 = "a"
input_3 = "aaaa"

input_list = [(len(input_1), input_1, 'first'), (len(input_2), input_2, 'second'),
              (len(input_3), input_3, 'third')]
input_list.sort(reverse=True)
print(input_list)
if input_list[0][0] != input_list[1][0] + input_list[2][0]:
    print("Cannot be solved")
    sys.exit()

if solve(input_list[0][1], input_list[1][1], input_list[2][1]):
    print("The %s can be solved by merging other two"%input_list[0][2])
else:
    print("Cannot be solved end")
sys.exit()