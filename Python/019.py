# Project Euler | Problem 19 | Jacob Waters
# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# 171
# date : 2015.07.20

import datetime


def countSunday(start, end):
    count = 0
    date = start

    while (date != end):
        if (date.weekday() == 6 and date.day == 1):
            count = count + 1
        date += datetime.timedelta(days=1)
    return count


print countSunday(datetime.date(1901, 01, 01), datetime.date(2000, 12, 31))
