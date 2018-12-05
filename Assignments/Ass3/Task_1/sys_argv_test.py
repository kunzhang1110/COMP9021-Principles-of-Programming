import sys

# 1. check if any options are valid
# 2. check file name ends with txt
# 3. check file exist in directory

def check_file_name(fn):
    # check file name ends with .txt
    if fn[-4:] == ".txt":
        return True
    return False


def check_grow_direction(gd):
    # grow direction should be either down, up, left, right or empty
    if gd in ["down", "up", "left", "right", ""]:
        return True
    return False


def check_node_style(gd):
    # node style should be either rectangle, circle, ellipse or empty
    if gd in ["rectangle", "circle", "ellipse", ""]:
        return True
    return False


def print_invocation():
    print("Incorrect invocation")
    sys.exit()


input_args = sys.argv[1:]

grow_direction = ""
node_style = ""
file_name = ""

if len(input_args) not in [1, 3, 5]:
    print_invocation()
    # Check file name

opt_args = list(zip(input_args[:-1:2],input_args[1:-1:2]))

for opt, arg in opt_args:
    if opt == "-nodestyle":
        node_style = arg
    elif opt == "-grow":
        grow_direction = arg
    else:
        print_invocation()

if check_grow_direction(grow_direction) and check_node_style(node_style):
    pass
else:
    print_invocation()

file_name = input_args[-1]
if not check_file_name (file_name):
        print_invocation()
try:
    fh = open(file_name, 'r')
except FileNotFoundError:
    print("No file named {} in current directory".format(file_name))
    sys.exit()

print(grow_direction, node_style, file_name)