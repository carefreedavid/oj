import csv
import sys

print "Howzit, which file are we chopping?"
csv_file = raw_input("> ")
print "here is the result"
print "--<----<---"

# testy = open('test.csv',"rb")

# prints reader
# reader = csv.reader(testy)

keep_list = []
# turns reader into a dic
with open(csv_file) as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         keep = row['']
         print keep
