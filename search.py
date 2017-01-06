import csv
import sys
import defy

# prompt user to enter city to search
restart = 'now'
while restart == 'now':
    print "Which city do you want to search?"
    print "~ cape town, durban, joburg, pretoria ~"
    answer = raw_input("> ")

    # reads jhb csv
    if answer == 'joburg':
        defy.index(answer)
        if defy.circle() == '':
            restart = ''

    # reads ct csv
    elif answer == 'cape town':
        defy.index(answer)
        if defy.circle() == '':
            restart = ''

    # read dbn csv
    elif answer == 'durban':
        defy.index(answer)
        if defy.circle() == '':
            restart = ''

    # read pta csv
    elif answer == 'pretoria':
        defy.index(answer)
        if defy.circle() == '':
            restart = ''

    else:
        print "Something went wrong, try again using one of these:"
        print "cape town, durban, joburg, pretoria"
        print "-------------------------------------------------"
