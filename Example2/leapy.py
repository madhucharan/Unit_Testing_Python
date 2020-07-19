def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return ("{0} is a leap year".format(year))
            else:
                return ("{0} is not a leap year".format(year))
        else:
            return ("{0} is a leap year".format(year))
    else:
        return ("{0} is not a leap year".format(year))

isLeapYear(2020)