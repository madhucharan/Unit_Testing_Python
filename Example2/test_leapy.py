# import leapy
#here we tried to import it in another way from above example
# from Example2.leapy import isLeapYear
import re
from leapy import *
def test_isleapyear():
    assert isLeapYear(2020) == "2020 is a leap year"
    # value =isLeapYear(2020)
    # assert re.match("2020 is a leap year",value)
