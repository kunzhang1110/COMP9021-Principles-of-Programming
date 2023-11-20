# Runs the Gale-Shapley algorithm for the stable marriage problem.
# Lets the user input names, or uses the default names M_1, ..., M_n for men
# and W_1, ..., W_n for women, where n is the number of couples,
# input by the user.
# Either lets the user define preferences or randomly generates preferences.
#
# Written by Eric Martin for COMP9021


from random import randint


def get_problem_size_and_names():
    while True:
        try:
            problem_size = int(input('Enter a strictly positive number '
                                     'for the number of couples: '))
            if problem_size <= 0:
                raise ValueException
            break
        except:
            print('\nIncorrect value, try again.')
    men = get_names(problem_size, 'men', 'M')
    women = get_names(problem_size, 'women', 'W')
    return problem_size, men, women

def get_names(problem_size, gender, default_name):
    print()
    while True:
        try:
            individuals = input('Enter {0:} names for the {1:}, '
                                'all on one line and separated by spaces,\n'
                                'or just press Enter for the default '
                                '"names" {2:}_1, ..., {2:}_{0:}: '
                                .format(problem_size, gender,
                                        default_name)).split()
            if len(individuals) == 0:
                for i in range(1, problem_size + 1):
                    individuals.append(default_name + '_' + str(i))
            elif len(set(individuals)) != problem_size:
                raise ValueException
            break
        except:
            print('\nYou did not give me {:} distinct names, '
                  'try again.'.format(problem_size))
    return individuals

def get_preferences(problem_size, men, women):
    user_choice = input('\nPress Enter to get a default preference '
                        'for all men or women.\n'
                        'Otherwise, input one or more nonspace characters '
                        'before Enter\n'
                        'to be prompted and enter the preferences '
                        'of your choice: ').split()
    if user_choice:
        men_preferences = get_preferences_from_user(problem_size,
                                                    men, women, True)
        women_preferences = get_preferences_from_user(problem_size,
                                                      women, men, False)
    else:
        men_preferences = get_random_preferences(problem_size,
                                                 men, women, True)
        women_preferences = get_random_preferences(problem_size,
                                                   women, men, False)
    return men_preferences, women_preferences

def get_random_preferences(problem_size, gender_1, gender_2, gender_1_is_male):
    gender_1_preferences = {}
    print()
    for individual in gender_1:
        preferences = list(gender_2)
        for i in range(problem_size - 1):
            j = randint(i, problem_size - 1)
            preferences[i], preferences[j] = preferences[j], preferences[i]
        print('Preferences for {:}: '.format(individual), end = '')
        for preference in preferences:
            print(preference, end = ' ')
        print()
        record_preferences(problem_size, individual,
                           gender_1_preferences, gender_1_is_male,
                           preferences)
    return gender_1_preferences

def get_preferences_from_user(problem_size, gender_1, gender_2,
                              gender_1_is_male):
    print()
    gender_2_set = set(gender_2)
    gender_1_preferences = {}
    for individual in gender_1:
        while True:
            try:
                preferences = input('List preferences for {:}, '
                                    'in decreasing order: '.
                                    format(individual)).split()
                if len(preferences) != problem_size or \
                                       set(preferences) != gender_2_set:
                    raise ValueException
                record_preferences(problem_size, individual,
                                   gender_1_preferences, gender_1_is_male,
                                   preferences)
                break
            except:
                print('\nInput is incorrect, try again.')
    return gender_1_preferences

def record_preferences(problem_size, individual, gender_preferences,
                       gender_is_male, preferences):
    if gender_is_male:
        # We reverse each man's list of preferences,
        # so chosing the preferred woman is effectively achieved
        # by popping (the last element) from that list.
        gender_preferences[individual] = sorted(preferences, reverse = True)
    else:
        # For women, it is convenient to explicitly record each man's rank
        # in her preferences rather than implicitly via the index of a list.
        gender_preferences[individual] = {preferences[i] : i
                                               for i in range(problem_size)}
       
def determine_stable_matching(men_preferences, women_preferences):
    free_men = set(men_preferences)
    # Will record both name and rank of men as algorithm is run.
    women_acceptances = {}
    while free_men:
        man = free_men.pop()
        woman = men_preferences[man].pop()
        if woman not in women_acceptances:
            women_acceptances[woman] = man, women_preferences[woman][man]
        elif women_preferences[woman][man] < women_acceptances[woman][1]:
            free_men.add(women_acceptances[woman][0])
            women_acceptances[woman] = man, women_preferences[woman][man]
        else:
            free_men.add(man)
    return {woman : women_acceptances[woman][0] for woman in women_acceptances}

def run_algorithm():
    men_preferences, women_preferences = \
                                get_preferences(*get_problem_size_and_names())
    matches = determine_stable_matching(men_preferences, women_preferences)
    print('\nThe matches are:')
    for woman in matches:
        print('{:} -- {:}'.format(woman, matches[woman]))

                    
                
                
            
