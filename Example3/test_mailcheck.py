import re

from mailcheck import *

def test_check():
    #we use re module functions for matching strings in first assert statement
    value = check("contact@gmail.com")
    assert re.match("Valid Email",value)
    #this should fail as it is not a vaild email
    assert check("madhucharan") == "Valid Email"