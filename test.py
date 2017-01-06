import csv
import sys

print "Howzit, which file are we chopping?"
answer = raw_input("> ")
print "here is hte result"
print "--<----<---"

# testy = open('test.csv',"rb")

# prints reader
# reader = csv.reader(testy)

keep_list = []
# turns reader into a dic
with open(answer) as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         keep = row['keep']
         print keep
