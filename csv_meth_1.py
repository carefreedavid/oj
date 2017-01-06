import csv
import sys
import defy

jhb_file = open('jhb.csv',"rb")
ct_file = open('ct_reg.csv',"rb")

print " --- Here are some areas in %s ---" % answer
print ""

  reader = csv.reader(jhb_file)

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
