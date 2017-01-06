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

# reads CT csv file
elif answer == 'ct':
    # allows the user to select section of CT for suggestions for subburbs
    subburb = ""
    print "-------------------------------------------"
    print "Which area in CT would you like to search?"
    print "-------------------------------------------"
    print "~type yes if you want suggestions~"
    print " "
    subburb = raw_input("> ")

    while subburb == 'yes':

            print """
            City Bowl                   South Peninsula
            Northern Suburbs	        Cape Flats
            Atlantic Seaboard	        Helderberg
            Southern Suburbs            West Coast
            """
            print "Which area in CT would you like to search?"
            subburb = raw_input("> ")

    print "-------------------------------------------"
    print "Here are the results for the %s" % subburb
    print "-------------------------------------------"

    keep_list = []
    # turns reader into a dic
    with open('ct.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            keep = row[subburb]
            print keep

else:
    print "something went wrong"
