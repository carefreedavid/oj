import csv
import sys
import defy

jhb_file = open('jhb.csv',"rb")
ct_file = open('ct_reg.csv',"rb")

# prompt user to enter city to search
print "Which city are you wanting to search?"
answer = raw_input("> ")

# loop while answer does not match results
while answer != 'dbn' and answer != 'joburg':
    print "hmmm, don't have that. Maybe try ct or joburg?"
    answer = raw_input("> ")

# reads joburg csv file and allocates it to 'reader' variable
if answer == 'joburg':
    defy.index(answer)

# reads CT csv file
elif answer == 'ct' or answer == 'Cape Town':
    defy.index(answer)

elif answer == 'dbn':
    defy.index(answer)

else:
    print "something went wrong"
