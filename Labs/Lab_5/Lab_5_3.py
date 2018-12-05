def get_month(month_name, start_day):
    last_day = month_lengths[month_names.index(month_name)]
    last_day += 1
    all_day_in_month = [" "]*(start_day-1) + [str(x) for x in range(1, last_day)]
    all_line_month = []
    week_line = ""
    for d in range(len(all_day_in_month)):
        week_line += "{:>2}".format(all_day_in_month[d])
        week_line += " "
        if (d+1) % 7 == 0:
            all_line_month.append(week_line)
            week_line = ""
    week_line += " "*(21 - len(week_line))
    all_line_month.append(week_line)   # append last line
    return len(all_day_in_month) % 7 + 1, all_line_month  # start day of next month


def print_year(year_name):
    def print_row(m1, m2, m3, mon_num):
        max_len = max(len(m1), len(m2), len(m3))
        print("{}{}{}".format(month_names[mon_num].center(23), month_names[mon_num+1].center(23), month_names[mon_num+2].center(23)))
        print('Mo Tu We Th Fr Sa Su\t'*3)
        for k in range(max_len): # k is the line number
            try:
                print(m1[k], end="\t")
            except IndexError:
                print(" "*len(m1[1]), end="\t")
            try:
                print(m2[k], end="\t")
            except IndexError:
                print(" "*len(m2[1]), end="\t")
            try:
                print(m3[k])
            except IndexError:
                print(" "*len(m3[1]))
        print('\n', end="")

    print("{:35}\n".format(year_name))
    number_of_leap_year = (year_name - 1752)//4 - (year_name - 1752)//100 + (year_name - 1752)//400 -1
    year_start_day = ((year_name - 1753) * 365 + number_of_leap_year) % 7 + 1
    start_day = year_start_day + 1
    for mon_number in range(len(month_names)):
        if (mon_number+1) % 3 == 1:
            start_day, first_month= get_month(month_names[mon_number], start_day)
        if (mon_number+1) % 3 == 2:
            start_day, second_month= get_month(month_names[mon_number], start_day)
        if (mon_number+1) % 3 == 0:
            start_day, third_month= get_month(month_names[mon_number], start_day)
            print_row(first_month, second_month, third_month, mon_number-2)
    return


def print_month(month_name, year_name):
    number_of_leap_year = (year_name - 1752)//4 - (year_name - 1752)//100 + (year_name - 1752)//400 -1
    year_start_day = ((year_name - 1753) * 365 + number_of_leap_year) % 7 + 1
    start_day = year_start_day + 1
    for mon_number in range(len(month_names)):
            start_day, next_month= get_month(month_names[mon_number], start_day)
            if month_names[mon_number][:3] == month_name:
                break
    print("    {}    {}".format(month_names[mon_number], year_name))
    print('Mo Tu We Th Fr Sa Su')
    for line in next_month:
        print(line)
    return

month_names = ['January', 'February', 'March', 'April',
                'May', 'June', 'July', 'August',
                'September', 'October', 'November', 'December']

user_input = input('''I will display a calender, either for a year or for a month in a year.
The earliest year should be 1753.
For the month, input at least the first three letters of the month's name.
Input year, or year and month, or month and year:''')

user_input = user_input.split()
month_name = False
print(len(user_input))
if len(user_input) == 1:
    year_name = int(user_input[0])
else:
    try:
        year_name = int(user_input[0])
        month_name = user_input[1]
    except ValueError:
        year_name = int(user_input[1])
        month_name = user_input[0]

if year_name%400 == 0 or (year_name%4 == 0 and year_name%100 !=0):
    month_lengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month_name:
    print_month(month_name, year_name)
else:
    print_year(year_name)