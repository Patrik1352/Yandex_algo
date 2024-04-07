def visocos_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True


def day_of_week_known_first_day( day_number, first_day_of_year):

    # Названия дней недели
    days_of_week = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}


    first_day_of_year = list(days_of_week.keys())[list(days_of_week.values()).index(first_day_of_year)]
    # Считаем день недели для заданного номера дня
    day_of_year = (first_day_of_year + day_number - 1) % 7
    return days_of_week[day_of_year]


def day_of_year(month_name, day, year):
    """Возвращает номер дня в году для заданной даты."""
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if visocos_year(year):
        days_in_months[1] = 29  # Февраль в високосном году имеет 29 дней

    month_to_number = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    month = month_to_number[month_name]

    return sum(days_in_months[:month - 1]) + day


n = int(input())
year = int(input())
list_of_num_holyday = []
for i in range(n):
    holydays = input().split(' ')
    day = int(holydays[0])
    month_name = holydays[1]
    list_of_num_holyday.append(day_of_year(month_name, day, year))
first_day_of_year = input()


days_of_week = {"Sunday":0, "Monday":0,"Tuesday":0, "Wednesday":0, "Thursday":0,  "Friday":0,  "Saturday":0}

for day_number in range(1, 366+(1 if visocos_year(year) else 0)):

    if day_number in list_of_num_holyday:
        day_to_exclude = day_of_week_known_first_day(day_number, first_day_of_year)
        updated_days_of_week = {day: value + 1 if day != day_to_exclude else value for day, value in
                                days_of_week.items()}
    else:
        days_of_week[day_of_week_known_first_day(day_number, first_day_of_year)] += 1
max_key = max(days_of_week, key=days_of_week.get)
min_key = min(days_of_week, key=days_of_week.get)
print(max_key, min_key)


