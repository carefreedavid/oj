import csv
import sys

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
