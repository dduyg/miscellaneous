# -*- coding: utf-8 -*-
""""q1-u488640.ipynb

"""

def is_palindrome(astr):
    # Converting input string to lowercase and remove space
    astr = astr.lower().replace(" ", "")
    # Checking if the reversed string is equal to original string
    return astr == astr[::-1]

is_palindrome("madam")
