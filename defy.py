import csv
import sys

# a function that gives the user a set of suggestions and returns subburbs in an area.
ct_file = 'ct.csv'
ct_sub = 'ct_sub.csv'
dbn_file = 'dbn.csv'
dbn_sub = 'dbn_sub.csv'
jhb_file = 'jhb.csv'

def index(area):

    if area == 'ct':
        filey = ct_file
        sub = ct_sub
    elif area == 'dbn':
        filey = dbn_file
        sub = dbn_sub
    elif area == 'joburg':
        filey = jhb_file
        sub = ct_sub

    print """
-------------------------------------------
Which area in %s would you like to search?
-------------------------------------------
~ type \'y\' if you want some suggestions ~

    """ % area

    subburb = raw_input("> ")

    while subburb == 'y':

            print """
------------------------------------------
suggested subburb searches
------------------------------------------"""

            keep_list = []
            # turns reader into a dic
            with open(sub) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    keep = row['sub']
                    print keep

            print "Which area in %s would you like to search?" % area
            subburb = raw_input("> ")

    print "-------------------------------------------"
    print "Here are the results for the %s" % subburb
    print "-------------------------------------------"

    keep_list = []
    # turns reader into a dic
    with open(filey) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            keep = row[subburb]
            print keep

# print result
