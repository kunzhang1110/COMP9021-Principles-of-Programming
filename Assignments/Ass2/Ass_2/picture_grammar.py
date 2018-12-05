# Assignment 2 for COMP2091
# Written by Kun Zhang (5076804)
# Sep 25, 2015
# -----------------------------------------------------------------------
import re
import sys
import copy

def get_grammar(fn):
    axiom_array, row_tables_group, column_tables_group = get_line(fn)
    axiom_array = check_axiom(axiom_array)
 #   print(column_tables_group)
    row_tables, row_epsilon = check_table_group(row_tables_group)
    column_tables, column_epsilon = check_table_group(column_tables_group)
    if row_epsilon and column_tables:
        print_error()
    if column_epsilon and row_tables:
        print_error()
    return axiom_array, row_tables, column_tables

def check_table_group(table_group):
    all_tables = []
    table_group_length = len(table_group)
    i = 0
    j = 0
    epsilon_flag = 0
    while i < table_group_length and j < table_group_length:
        if table_group[i] == '\n':
            i += 1
        else:
            start_index = i
            j = i
            while table_group[j] != '\n':
                j += 1
                if j == table_group_length:
                    break
            end_index = j
            table_stripped, epsilon_flag = check_tables(table_group[start_index:end_index])
            all_tables.append(table_stripped)
            i = j
    return all_tables, epsilon_flag


def check_tables(table):
    """Check the validity of an row table by:
    1. No blank line between lines
    2. no repetitive left-hand side
    3. each right hand side has same number of tokens or symbols
    4. if one rule has ε on the right all rules must have ε on the right
    returns stripped table
    """
#    print('table', table)
    prev_blank_flag = 0     # 0 if blank
    positive_edge_count = 0  # count the number of 0 -> 1 for blank_flag
    table_stripped =[]
    all_left_hand = []
    pre_right_hand = []
    epsilon_flag = 0
    for rule in table:
        match_result = re.match(r'[\s]+',rule)
        if match_result:     # if blank line
            blank_flag = 0
        else:
            blank_flag = 1
            left_hand, right_hand = check_rule(rule)
            if left_hand in all_left_hand:
#                print("Table Error 2: repetitive left hand")
                print_error()
            else:
                all_left_hand.append(left_hand)
            if not pre_right_hand:
                pre_right_hand = right_hand
            if len(right_hand) != len(pre_right_hand):
#                print("Table Error 3: not having the same number on the right")
                print_error()
            if pre_right_hand == ['ε']:
                epsilon_flag = 1
                if right_hand != pre_right_hand:
#                    print("Table Error 4: not all ε")
                    print_error()
            pre_right_hand = right_hand
            left_hand = left_hand.strip()
            for i in range(len(right_hand)):
                right_hand[i] = right_hand[i].strip()
            table_stripped.append((left_hand, right_hand))
        if prev_blank_flag == 0 and blank_flag == 1:
            positive_edge_count += 1
        if positive_edge_count == 2:
#            print("Table Error 2: Blank line in between")
            print_error()
        prev_blank_flag = blank_flag
    return table_stripped, epsilon_flag


def check_rule(rule):
    """Check the validity of a rule by:
    1. left: 1 token
    2. followed by ->
    3. right: one or more token or symbol
    4. if one rule has ε on the right then right hand side has nothing else
    5. valid token and symbols
    """
    pattern = re.compile(r"^([^\d\W][\w\s]*) -> ([\w\W\s]*)", re.ASCII)
    match_object = re.match(pattern, rule)
    if not match_object:
#        print("Rule Error 1,2, 3: Not correct format")
        print_error()
    else:
        left_hand = match_object.group(1)
        right_hand = match_object.group(2)
        right_hand_list = right_hand.split()
        for e in right_hand_list:
            if check_symbol(e,'Table') or check_token(e):
                if check_symbol(e,'Table') == 'ε':
                    if len(right_hand_list) != 1:
#                        print('Rule Error 4: More than ε')
                        print_error()
            else:
#                print("Rule Error 5: Not valid token/symbols")
                print_error()
  #  print(left_hand, right_hand_list)
    return left_hand, right_hand_list


def check_axiom(axiom_array):
    """Check the validity of an axiom by:
    1. Number of lines > 0
    2. No blank line between lines
    3. Tokens and symbols are valid separated by spaces
    4. no ε
    returns stripped axiom_array
    """

    prev_blank_flag = 0     # 0 if blank
    positive_edge_count = 0  # count the number of 0 -> 1 for blank_flag
    axiom_array_stripped =[]
    for axa in axiom_array: # for each line in axiom array
        match_result = axa.isspace()
        if match_result:     # if blank line
            blank_flag = 0
        else:
            blank_flag = 1
            for e in axa.split():
                if check_symbol(e,'Axiom') or check_token(e):
                    pass
                else:
#                    print("Axiom Error 3,4: Not valid token/symbols")
                    print_error()
            axiom_array_stripped.append(axa)
        if prev_blank_flag == 0 and blank_flag == 1:
            positive_edge_count += 1
        if positive_edge_count == 2:
 #           print("Axiom Error 2: Blank line in between")
            print_error()
        prev_blank_flag = blank_flag
#        print('axa', axa.split(), positive_edge_count)   # for every element in axa
    if positive_edge_count == 0 and blank_flag == 0:
#            print("Axiom Error 1: No Lines")
            print_error()
    return axiom_array_stripped


def check_token(e):
    """Gets valid symbol otherwise returns False
    A valid token is given by:
    1. only having alphabet or digit or underscore
    2. starting with non_digit
    """
    pattern = re.compile(r"^[^\d\W]\w*\Z", re.ASCII)    # ASCII characters
    match_result = re.match(pattern, e)
    if not match_result:
        return False
#    print('token', e)
    return True


def check_symbol(e, flag):
    """Gets valid token otherwise prints error
    Valid token is given by:
    1. any non-space character
    """
    pattern = re.compile(r"[^\s]{1}\Z", re.ASCII)
    match_result = re.match(pattern, e)
    if match_result == None:
        return False
    if flag == 'Axiom':
        if e == 'ε':
#            print('Symbol ε')
            print_error()
    if flag == 'Table':
        if e == 'ε':
#            print('Symbol ε')
            return 'ε'
#    print('symbol', e)
    return True


def get_line(fn):
    """ Get axiom array, row table and column table"""
    fh = open(fn, 'r', encoding='utf-8')
    column_table_list = []
    axiom_array_list = []
    row_table_list = []
    all_hash_header = ["# Column tables\n", "# Row tables\n", "# Axiom array\n"]
    i = 0   # counter for all_line
    hash_flag = 'Initial'
    for line in fh:
        if line == hash_flag: # error if exists redundant hash headers
                print_error()

        if line in all_hash_header: # get hash flag
            hash_flag = line
            all_hash_header.remove(line)


        if line != '':        # use hash flag to save to destined variables
            if hash_flag == "# Column tables\n":
                column_table_list.append(line)
            if hash_flag == "# Row tables\n":
                row_table_list.append(line)
            if hash_flag == "# Axiom array\n":
                axiom_array_list.append(line)

    if all_hash_header:         # error if less than three hash headers
        print_error()

    return axiom_array_list[1:], row_table_list[1:], column_table_list[1:]  # do not return hash headers


def print_error():
    print("Incorrect grammar")
    sys.exit()


def print_tables(tables):
    for group in tables:
        group.sort()        # lexicographic order
        max_left_width = max([len(l.strip()) for l, r in group]) + 1
        max_right_width = max([len(t.strip()) for l, r in group for t in r]) + 1
        for left, right in group:
            print("{0:{1}}".format(left, max_left_width), end='')
            print("{:<3}".format('->'), end='')
            for r in right:
                if r == 'ε':
                    print(' ', end="")
                else:
                    print("{0:{1}}".format(r, max_right_width), end='')
            print('\n', end='')
        print('\n', end='')


def print_pattern(array):
    max_width = max([len(t.strip()) for line in array for t in line]) + 1
    for line in array:
        line_list = line.split()
        for ll in line_list:
            print("{0:{1}}".format(ll.strip(), max_width), end='')
        print('\n', end='')


def symbols(grammar_in):
    axiom_array, row_tables, column_tables = grammar_in
    all_left = []
    all_right = []
    terminals = []
    for group in row_tables:
        for left, right in group:
            all_left.append(left.strip())
            for r in right:
                all_right.append(r.strip())
    for group in column_tables:
        for left, right in group:
            all_left.append(left.strip())
            for r in right:
                all_right.append(r.strip())
    non_terminals = set(all_left)
    non_terminals = list(non_terminals)
    non_terminals.sort()
    for ar in all_right:
        if ar not in non_terminals:
            terminals.append(ar)
    terminals = set(terminals)
    terminals = list(terminals)
    terminals.sort()
    return non_terminals, terminals


def check_final_pic(final_pic, final_pic_length, axiom_array, terminals):
    """Check validity of the final picture"""

    axiom_array_string = "".join(axiom_array)
    if final_pic_length < len(axiom_array_string):
        print(final_pic_length)

    final_pic_split = final_pic.split()
    line_length = len(final_pic_split[0])
    for line in final_pic_split:
        if len(line)!= line_length:
            print_invalid()
        for char in line:
            if char not in terminals:
                print('here')
                print_invalid()
    return final_pic_split


def generate(grammar_in, final_picture):
    """Generate deterministic final part and check final_picture's validity"""
    # final picture should be in form of 's_1\ns_2\ns_N'
    axiom_array, row_tables, column_tables = grammar_in
    non_terminals,terminals =symbols(grammar_in)
    try:
        final_picture_total = len(final_picture)
    except IndexError:
        print_invalid()
    # check validity of final picture
    final_split = check_final_pic(final_picture, final_picture_total, axiom_array, terminals)
    final_list = []
    for s in final_split:
        final_list.append([x for x in list(s)])
    final_picture_length = (len(final_list), len(final_list[0])) # No, of row, No. of column
    axiom_list = []
    for axiom in axiom_array:
        axiom_list.append(axiom.split())
    all_generated_list=[]
    all_deter_list=[]
    if generate_new_pic(axiom_list, grammar_in, final_list, all_generated_list, final_picture_length, all_deter_list):
        cof = (len(row_tables)+1) * len(column_tables)
        if len(all_generated_list) > cof * len(all_deter_list):
            print("Picture cannot be generated in only one way.")
            print('Here is the final deterministic part:')
        else:
            print("Picture can be generated in only one way.")
            print('Here it is:')

        for i in range(len(all_deter_list[::-1])): # for every block
            max_width = max([len(x) for h in all_deter_list[::-1][i] for x in h]) + 1   # get max width for every block
            for j in all_deter_list[::-1][i]:     # for every row
                for k in j: # for every element
                #    print(k, end=" ")
                    print("{0:{1}}".format(k, max_width), end='')
                print("\n", end="")
            if len(all_deter_list[::-1]) != i:
                print("\n", end="")
    else:
        print("Picture cannot be generated")


def generate_new_pic(current_pic, grammar_in, final_list,all_gen_list, final_picture_length, all_deter_list):
    """Generate a new_pic and check if it is the desried one"""
    axiom_array, row_tables, column_tables = grammar_in
    non_terminals,terminals =symbols(grammar_in)
    if current_pic in all_gen_list: # store explored pictures
        if current_pic in all_deter_list:   # if the stored picture is in the deterministic list
            return True
        return False
    all_gen_list.append(current_pic) # store not-yet-explored pictures
    if not check_generated_pic(current_pic, final_picture_length, final_list):
        return False
    if current_pic == final_list:
        all_deter_list.append(current_pic)
        return True
    current_pic_transposed = transpose(current_pic)
    # find all the non_terminals
    row_table_non_terminals = []
    for table in row_tables:
        row_table_non_terminals.append([rule[0] for rule in table])
    column_table_non_terminals = []
    for table in column_tables:
        column_table_non_terminals.append([rule[0] for rule in table])
    # check if there is a column can  be applied by rules
    group_col = []  # store group_ind and col_ind
    for group_ind in range(len(column_table_non_terminals)):
        for col_ind in range(len(current_pic_transposed)): # for each row
            col_match_count = 0
            for element in current_pic_transposed[col_ind]: # for each element
                if element in column_table_non_terminals[group_ind]:
                    col_match_count += 1
                if col_match_count == len(current_pic_transposed[col_ind]):
                    group_col.append((group_ind, col_ind))
    for group_ind, col_ind in group_col:
        step_picture = copy.deepcopy(current_pic)   # create a new list object
        for row_ind in range(len(current_pic)):
            for rule in column_tables[group_ind]:
                if rule[0] == current_pic[row_ind][col_ind]:
                    step_picture[row_ind][col_ind] = rule[1]   # replace with terminal
                    step_picture[row_ind] = unchain(step_picture[row_ind])
        if generate_new_pic(step_picture, grammar_in, final_list, all_gen_list, final_picture_length, all_deter_list):
            all_deter_list.append(current_pic)
            return True
    # check if there is a row can  be applied by rules
    group_row = []
    for group_ind in range(len(row_table_non_terminals)):
        for row_ind in range(len(current_pic)): # for each row
            row_match_count = 0
            for element in current_pic[row_ind]: # for each element
                if element in row_table_non_terminals[group_ind]:
                    row_match_count += 1
                if row_match_count == len(current_pic[row_ind]):
                    group_row.append((group_ind, row_ind))
    for group_ind, row_ind in group_row:
        step_picture = copy.deepcopy(current_pic_transposed)
        for col_ind in range(len(current_pic_transposed)):
            for rule in row_tables[group_ind]:
                if rule[0] == current_pic_transposed[col_ind][row_ind]:
                    step_picture[col_ind][row_ind] = rule[1]   # replace with terminal
                    step_picture[col_ind] = unchain(step_picture[col_ind])
        if generate_new_pic(transpose(step_picture), grammar_in, final_list, all_gen_list, final_picture_length, all_deter_list):
            all_deter_list.append(current_pic)
            return True
    return False

def check_generated_pic(generated_pic, final_pic_length, final_pic):
    """check if generated picture is larger than required"""
    generated_picture_length = (len(generated_pic), len(generated_pic[0]))
    if (generated_picture_length[0] > final_pic_length[0]) or (generated_picture_length[1] > final_pic_length[1]):
        return False
    return True
    # elif generated_picture_length == final_pic_length and generated_pic != final_pic:
    #     return False
    # else:


def transpose(ls):
    """Return a transposed matrix"""
    transposed_ls = [list(x) for x in zip(*ls)]
    return transposed_ls


def unchain(ls):
    """Unchain a nested list"""
    b = []
    for i in range(len(ls)):
        if type(ls[i]) is list:
            for x in ls[i]:
                b.append(x)
        else:
            b.append(ls[i])
    return b


def print_invalid():
    print('Picture is invalid')
    sys.exit()



