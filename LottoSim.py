import random
import sys
import time


def computer_random():
    """let the computer create a list of 6 unique random integers from 1 to 59"""
    ci = random.sample(range(1, 60), 6)
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
            else:
                print("Wrong number or number already used!")
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

# TO DO make sure no other numbers that are not 3,4,5,6 can be used for this
# user numbers and number of matches are required to calculate the number of draws for usernumbers to reach the required match
def matchdraw(usernumbers, matchno):
    """User numbers should be in form of a list. matchno - int between 3 and 6"""
    match = 0
    stat = 0
    user_list = usernumbers
    while match == 0:
        comp_list = computer_random()
        print('Draw no {} '.format(stat))
        matches = match_lists(comp_list, user_list)
        stat += 1
        if matches == matchno:
            match = 1
    return ('Your numbers {} has been matched after: {} draws'.format(user_list,stat))


print(matchdraw(computer_random(),3))
#result_list = []
#for x in range(1, 60):
    #result_list.append(match3draw(computer_random(), 4))

# average of the draws required to match 3 with user lucky dip
#print(sum(result_list) / len(result_list))
