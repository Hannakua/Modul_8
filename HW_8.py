from datetime import datetime, date, timedelta

days_name = {
   0: "понеділок",
   1: "вівторок",
   2: "середа",
   3: "четвер",
   4: "п'ятниця",
   5: "субота",
   6: "неділя",
}

from collections import defaultdict
users_example = [
        {'Tarasko Ivan': date(year=1979, month=4, day=25)},
        {'Konovalov Artem': date(year=1981, month=4, day=23)},
        {'Nagurna Stanislava':date(year=1973, month=4, day=22)}, 
        {'Chizhikov Oleg': date(year=1992, month=4, day=28)},
        {'Petrenko Daryna': date(year=2000, month=4, day=25)},
        {'Lutc Olga': date(year=1967, month=4, day=28)},
        {'Stepanova Maria': date(year=1974, month=4, day=29)},
        {'Grigorenko Iryna': date(year=1997, month=4, day=30)}
        ]

current_date = datetime.now()
next_week =current_date + timedelta(days=7)

print(f'сьогодні: {next_week.date()}')


def user_birth_weekend(date_birthday): # якщо день народження випадає на суботу/неділю функція змінює дату др на найближчий понеділок
        if date_birthday.weekday()==5:
                bithday_print_date=date_birthday.toordinal()+2
        elif date_birthday.weekday()==6:  
                bithday_print_date=date_birthday.toordinal()+1
        else:
                bithday_print_date=date_birthday.toordinal()
        return bithday_print_date # повертає перенесену дату дня народження      


def get_birthdays_per_week(users): # ф-ція вивода списку колег на тиждень вперед, яких треба привітати з др 
        dict_birth= defaultdict(list)
        for user in users:
                name, date_birth = user.popitem()
                date_dr_this_year = date(year=current_date.year, month=date_birth.month, day=date_birth.day)
                dr_ordinal = user_birth_weekend(date_dr_this_year)
                date_dr = date.fromordinal(dr_ordinal)
                if (next_week.toordinal() - dr_ordinal) in range(0, 7): 
                        number_day=date_dr.weekday()
                        day_name = days_name.get(number_day)                      
                        dict_birth[day_name].append(name)       

        for i in range(1,8): # виводимо впорядковано дні народження по дням тижня починаючи з завтрашнього дня
                day_week = current_date + timedelta(days=i) 
                number_day = day_week.weekday()
                day_name = days_name.get(number_day)            
                if day_name in dict_birth:               
                        print(day_name,': ', ', '.join(dict_birth.get(day_name)))


if __name__ == "__main__":  

        get_birthdays_per_week(users_example)


# Task

# Вам нужно реализовать полезную функцию для вывода списка коллег, 
# которых надо поздравить с днём рождения на неделе.

# У вас есть список словарей users, каждый словарь в нём обязательно имеет ключи name и birthday. 
# Такая структура представляет модель списка пользователей с их именами и днями рождения. 
# name — это строка с именем пользователя, а birthday — это datetime объект, в котором записан день рождения.

# Ваша задача написать функцию get_birthdays_per_week, которая получает на вход список users 
# и выводит в консоль (при помощи print) список пользователей, которых надо поздравить по дням.

# Conditions:

# get_birthdays_per_week выводит именинников в формате:
# Monday: Bill, Jill
# Friday: Kim, Jan

# Пользователей, у которых день рождения был на выходных, надо поздравить в понедельник.
# Для отладки удобно создать тестовый список users и заполнить его самостоятельно.
# Функция выводит пользователей с днями рождения на неделю вперед от текущего дня.
# Неделя начинается с понедельника.