from __future__ import print_function, division

from datetime import datetime


def main():
    print("Today's date and day of the week:")
    today = datetime.today()
    print(today)
    print(today.strftime("%A"))

    print("Your birthday and how long before it: ")
    # s = input ('Enter birth date in mm/dd/yyy format: ')
    s = '1/2/1992'
    bday = datetime.strptime(s, '%m/%d/%Y')

    next_bday = bday.replace(year=today.year)
    if next_bday < today:
        next_bday = next_bday.replace(year=today.year + 1)
    print(next_bday)

    until_next_bday = next_bday - today
    print(until_next_bday)

    print("Your age now: ")
    last_bday = next.bday.replace(year=next_bday.year - 1)
    age = last_bday.year - bday.year
    print(age)

    print("For those born on: ")
    bday1 = datetime(day=10, month=6, year=1962)
    bday2 = datetime(day=18, month=4, year=1965)
    print(bday1)
    print(bday2)

    print("Double Day is: ")
    d1 = min(bday1, bday2)
    d2 = max(bday1, bday2)
    dd = d2 + (d2 - d1)
    print(dd)

    if __name__ == '__main__':
        main()


"""Reference:
AllenDowney. (2015) ThinkPython2/code/double.py. Available from:
https://github.com/AllenDowney/ThinkPython2/blob/master/code/double.py [Accessed 28 December 2023]."""