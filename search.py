import csv
import sys
import defy

jhb_file = open('jhb.csv',"rb")
ct_file = open('ct_reg.csv',"rb")

# prompt user to enter city to search
restart = 'now'
while restart == 'now':
    print "Which city do you want to search?"
    print "~ cape town, durban, joburg, pretoria ~"
    answer = raw_input("> ")

# loop while answer does not match results
# while answer != 'pretoria' and answer != 'joburg':
    # print "hmmm, don't have that. Maybe try ct or joburg?"
    # answer = raw_input("> ")

# reads jhb csv
    if answer == 'joburg':
        defy.index(answer)
        restart = ''

        # reads CT csv
    elif answer == 'cape town' or answer == 'Cape Town':
        defy.index(answer)
        restart = ''

        # read dbn csv
    elif answer == 'durban':
        defy.index(answer)
        restart = ''

    elif answer == 'pretoria':
        defy.index(answer)
        restart = ''

    else:
        print "Something went wrong, try again using one of these:"
        print "cape town, durban, joburg, pretoria"
        print "-------------------------------------------------"
