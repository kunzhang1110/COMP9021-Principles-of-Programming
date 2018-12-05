# Calender Program



def month_print(month_number, year_number):
    number_of_leap_years = (year_number - 1752)//4 - (year_number - 1752)//100 + (year_number - 1752)//400
    total_days= (year_number - 1753) * 365 + number_of_leap_years
    leading_days_of_year = total_days % 7
    leading_days = (leading_days_of_year + sum(all_month_days[:month_number]))%7
    month_print_month(month_number,leading_days, year_number)


def check_leap_year(year_number):
    if (year_number% 400==0) or (year_number % 4 == 0 and year_number % 100 !=0):
        return True
    return False

def month_print_month(month_number,leading_days, year_number):
    print("{:>10}".format(all_month[month_number] + " " + str(year_number)))
    print("Mo Tu We Th Fr Sa Su")
    print("   "*leading_days, end="")
    for i in range(all_month_days[month_number]):
        print("{:>2} ".format(i+1), end="")
        remain_days = (leading_days + i+1) % 7
        if remain_days == 0:
            print("")
    return remain_days



def year_print_month(month_number,leading_days):
    all_line_txt = []
    line_txt ="   "*leading_days
    for i in range(all_month_days[month_number]):
        line_txt += "{:>2} ".format(i+1)
        remain_days = (leading_days + i+1) % 7
        if remain_days == 0 and line_txt:
            all_line_txt.append(line_txt)
            line_txt = ""
    if line_txt:
        line_txt += " " * (21 - len(line_txt))
        all_line_txt.append(line_txt)
    return all_line_txt, remain_days


def year_print(year_number):
    number_of_leap_years = (year_number - 1752)//4 - (year_number - 1752)//100 + (year_number - 1752)//400
    total_days= (year_number - 1753) * 365 + number_of_leap_years
    leading_days_of_year = total_days % 7
    print("{:>30}".format(year_number))
    leading_days = leading_days_of_year
    for month_number in range(0, len(all_month_days)-2):
        if month_number%3 == 0:
            print("{:24}  {:24}  {:24}".format(all_month[month_number], all_month[month_number+1], all_month[month_number+2]))
            print("Mo Tu We Th Fr Sa Su   "*3)
            month_1, leading_days = year_print_month(month_number,leading_days)
            month_2, leading_days = year_print_month(month_number+1,leading_days)
            month_3, leading_days = year_print_month(month_number+2,leading_days)
            max_len_month = max(len(month_1), len(month_2), len(month_3))
   #         print(month_1)
            for i in range(max_len_month):
                try:
                    print(month_1[i], end="  ")
                except:
                    print(" "*23, end="")
                try:
                    print(month_2[i], end="  ")
                except:
                    print(" "*24, end="")
                try:
                    print(month_3[i])
                except:
                    print("  "*24)
            print("")

all_month = ["January", "February", "March", "April", "May", "June", "July", "August",\
             "September", "October", "November", "December"]
all_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

user_in = input("Enter:")
user_input = user_in.split()
if len(user_input) ==1:
    try:
        year_number = int(user_input[0])
    except:
        print("Error")
    else:

        if check_leap_year(year_number):
            all_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
        year_print(year_number)
elif len(user_input) ==2:
    try:
        year_number = int(user_input[0])
    except:
        try:
            year_number = int(user_input[1])
        except:
            print("Error 2")
        else:
            for m in range(len(all_month)):
                if user_input[0] == all_month[m][:3]:
                    month_number = m
                    break
            month_print(month_number, year_number)
    else:
        for m in range(len(all_month)):
            if user_input[1] == all_month[m][:3]:
                month_number = m
                break
        month_print(month_number, year_number)

