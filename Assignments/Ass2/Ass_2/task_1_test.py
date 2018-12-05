  axiom_list_transposed = transpose(axiom_list)
#    print(axiom_list_transposed)
    all_covered_pic = []
    step_picture = copy.deepcopy(axiom_list)


    step_picture = list(axiom_list)
    for table in column_tables:     # apply rules from table
        step_picture = axiom_list
        for row_ind in range(len(step_picture)):
            target_non_terminal = step_picture[row_ind][target_column]
            for rule in table:
                if rule[0] == target_non_terminal: # if rule's non_terminal matches
                        step_picture[row_ind][target_column] = rule[1]   # replace with terminal
                        step_picture[row_ind] = unchain(step_picture[row_ind])
        print('Step picture:',step_picture, axiom_list)

    print(step_picture)




    step_picture = transpose(step_picture)
    prev_picture = copy.deepcopy(step_picture)



    for table in row_tables:     # apply rules from table
        step_picture = copy.deepcopy(prev_picture)
        for row_ind in range(len(step_picture)):
            target_non_terminal = step_picture[row_ind][target_column]
            for rule in table:
                if rule[0] == target_non_terminal: # if rule's non_terminal matches
                        step_picture[row_ind][target_column] = rule[1]   # replace with terminal
                        step_picture[row_ind] = unchain(step_picture[row_ind])
     #   print('Step picture:',step_picture, prev_picture)
    step_picture = transpose(step_picture)
    print(step_picture)












-----------------
    if row_index:
        for table in row_tables:
            step_picture = copy.deepcopy(current_pic_transposed)
            for r in range(len(step_picture)):
                target_non_terminal= step_picture[r][row_index]
                for rule in table:
                    if rule[0] == target_non_terminal: # if rule's non_terminal matches
                        step_picture[r][row_index] = rule[1]
                        step_picture[r] = unchain(step_picture[r])
  #      step_picture = transpose(step_picture)
        print(step_picture)
    else:
        current_pic_transposed = transpose(current_pic)
        for i in range(len(current_pic_transposed)):
            for e in current_pic_transposed[i]:
                if e not in non_terminals:
                    break
                column_index = i
                break


    for i in range(len(current_pic)):
        for e in current_pic[i]:
            if e not in non_terminals:
                break
            row_index = i
            break
    print(current_pic[i])
