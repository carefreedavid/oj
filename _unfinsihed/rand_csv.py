import csv
import sys
import random

keep_list = []
      # turns reader into a dic
with open('rand.csv') as f:
    d = dict(filter(None, csv.reader(f)))

print d 
