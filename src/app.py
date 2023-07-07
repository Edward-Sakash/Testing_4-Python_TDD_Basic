# Task 4
from random import randrange


# Function will return random number between start and end parameter where end is included
def rnd(start, end):
    return randrange(start, end + 1)


# Function should return the greatest number in a list
def max_num_in_list(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num




