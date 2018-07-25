import random
import sys
import time


def computer_random():
    """let the computer create a list of 6 unique random integers from 1 to 59"""
    comp_no = random.sample(range(1, 59), 6)
    return comp_no


user_list = [1,2,3,5,6,7]

def match_lists(list1, list2):
    """to find the number of matching items in each list use sets"""
    set1 = set(list1)
    set2 = set(list2)
    # set3 contains all items comon to set1 and set2
    set3 = set1.intersection(set2)
    # return number of matching items
    return len(set3)

print("Selected numbers:", user_list)
match3 = 0
match4 = 0
match5 = 0
match6 = 0

draws = 100

for k in range(draws):
    comp_list = computer_random()
    matches = match_lists(comp_list, user_list)
    if matches == 3:
        match3 += 1
    elif matches == 4:
        match4 += 1
    elif matches == 5:
        match5 += 1
    elif matches == 6:
        match6 += 1


print("Out of %d tickets sold the computer found these matches:" % draws)
print("3 matches = %d" % match3)
print("4 matches = %d" % match4)
print("5 matches = %d" % match5)
print("6 matches = %d" % match6)
