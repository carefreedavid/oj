# this script wants to allow the user to choose a region in the Cape Town area.

import csv
import sys

ct_file = open('ct_reg.csv',"rb")

reader = csv.reader(ct_file)

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

ct_file.close()
