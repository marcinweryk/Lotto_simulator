
import random
import sys
import time

def computer_random():
    """let the computer create a list of 6 unique random integers from 1 to 59"""
    ci = random.sample(range(1, 60), 6)
    #print("Computer draw", ci)
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
user_list = user_random()
print ("Selected numbers:", user_list)
# set up counters for 3 to 6 matches
match3 = 0
match4 = 0
match5 = 0
match6 = 0

# the computer picks the numbers for each ticket sold
tickets_sold = 100
print ("Just a moment ...")
stat = 0

for k in range(tickets_sold):
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
    # optional progress indicator
    if k % 140000 == 0:
        print(str(stat) + "% Completed")
        stat += 1

print("100% Completed")
print()
print("Out of %d tickets sold the computer found these matches:" % tickets_sold)
print("3 matches = %d" % match3)
print("4 matches = %d" % match4)
print("5 matches = %d" % match5)
print("6 matches = %d" % match6)
