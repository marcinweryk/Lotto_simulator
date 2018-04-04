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

def match3draw():
    match3 = 0
    stat = 0
    user_list = computer_random()
    #print("User numbers {}".format(user_list))
    while match3 == 0:
        comp_list = computer_random()
        #print("Draw number:{} - Computer numbers: {}".format(stat,comp_list))
        matches = match_lists(comp_list, user_list)
        stat += 1
        if matches == 3:
            match3 = 1
            #print("Computer numbers: {} on the draw number: {}".format(comp_list,stat))
    return stat

result_list = []
for x in range(1,60):
    result_list.append(match3draw())
    #print(match3draw())

print(sum(result_list)/len(result_list))
