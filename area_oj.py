import csv
import sys

# allows the user to select section of CT for suggestions for subburbs
subburb = ""
print """
-------------------------------------------
Which area in %s would you like to search?
-------------------------------------------
~ type \'y\' if you want some suggestions ~

""" % answer

subburb = raw_input("> ")

while subburb == 'y':

        print """
        ------------------------------------------
        suggested subburb searches
        ------------------------------------------"""
        print """
        City Bowl                  South Peninsula
        Northern Suburbs	    Cape Flats
        Atlantic Seaboard	    Helderberg
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
