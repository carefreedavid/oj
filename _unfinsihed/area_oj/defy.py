import csv
import sys

# a function that gives the user a set of suggestions and returns subburbs in an area.
ct_file = 'ct.csv'
ct_sub = 'ct_sub.csv'
dbn_file = 'dbn.csv'
dbn_sub = 'dbn_sub.csv'
jhb_file = 'jhb.csv'
pta_file = 'pta.csv'
pta_sub = 'pta_sub.csv'

def index(area):

    if area == 'cape town':
        filey = ct_file
        sub = ct_sub
    elif area == 'durban':
        filey = dbn_file
        sub = dbn_sub
    elif area == 'joburg':
        filey = jhb_file
        sub = ct_sub
    elif area == 'pretoria':
        filey = pta_file
        sub = pta_sub

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

            print """
---------------------------------------------
Which area in %s would you like to search?
---------------------------------------------""" % area
            subburb = raw_input("> ")

    print "-----------------------------------------------"
    print "Here are the results for the %s of %s" % (subburb, area)
    print "-----------------------------------------------"

    keep_list = []
    # turns reader into a dic
    with open(filey) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            keep = row[subburb]
            print keep

def circle():
    print "---"
    print "Do you want to search anything else? (yes or no)"
    answer = raw_input("> ")
    if answer == 'yes':
        restart = 'now'
    else:
        print "thank you, come again"
        restart = ''
        return restart
