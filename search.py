import csv
import sys

jhb_file = open('jhb_reg.csv',"rb")
ct_file = open('ct_reg.csv',"rb")
# add: CT, Durban, Pretoria, Stellenbosch, Hermanus, PE,

# prompt user to enter city to search
print "Which city are you wanting to search?"
answer = raw_input("> ")

# loop while answer does not match results
while answer != 'ct' and answer != 'joburg':
    print "hmmm, don't have that. Maybe try joburg?"
    answer = raw_input("> ")

# reads joburg csv file and allocates it to 'reader' variable
if answer == 'joburg':
    print " --- Here are some areas in %s ---" % answer
    print ""
    reader = csv.reader(jhb_file)
elif answer == 'ct':
    print " --- Here are some areas in %s ---" % answer
    print ""
    reader = csv.reader(ct_file)
else:
    print "something went wrong"

# returns results of the desired search relevant csv
rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row

    else:
        colnum = 0
        for col in row:
            print '%s' % col
            colnum += 1

    rownum += 1

jhb_file.close()
