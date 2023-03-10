# -*- coding: utf-8 -*-
"""assign2.ipynb
"""

def multi3_odd(start, finish):
    count = 0
    for num in range(start, finish+1):
        if num % 2 == 1 and num % 3 == 0:
            count += 1
    return count

multi3_odd(1, 10)
