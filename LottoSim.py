import random
import sys
import time


def computer_random():
    """let the computer create a list of 6 unique random integers from 1 to 59"""
    ci = random.sample(range(1, 59), 6)
    # print("Computer draw", ci)
    return ci


def user_random():
    """let the user create a list of 6 unique random integers from 1 to 59"""
    print("Enter 6 unique random integers from 1 to 59:")
    ui = []
    while len(ui) < 6:
        print(len(ui) + 1),
        try:
            i = int(input("--> "))
            # check if i is unique and has a value from 1 to 59
            # and is an integer, otherwise don't append1
            if (i not in ui) and (1 <= i <= 59) and type(i) == type(7):
                ui.append(i)
        except:
            print("Enter an integer number!")
    return ui


def match_lists(list1, list2):
    """to find the number of matching items in each list use sets"""
    set1 = set(list1)
    set2 = set(list2)
    # set3 contains all items comon to set1 and set2
    set3 = set1.intersection(set2)
    # return number of matching items
    return len(set3)


# the user picks the 6 winning numbers
# user_list = user_random()
# print ("Selected numbers:", user_list)
# set up counters for 3 to 6 matches
match3 = 0
match4 = 0
match5 = 0
match6 = 0

# the computer picks the numbers for each ticket sold
tickets_sold = 14000000
print("Selected numbers: 1, 2, 3, 4, 5, 6")
print("Just a moment ...")
stat = 0

while match3 == 0:
    comp_list = computer_random()
    user_list = (1, 2, 3, 4, 5, 6)
    matches = match_lists(comp_list, user_list)
    stat += 1
    if matches == 3:
        match3 = 1
        print("3 matched after {} of draws".format(stat))

