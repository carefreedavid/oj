import sys
import csv

alph_csv = 'alph.csv'

number = []
letter = []
count = []
addit = []

print "hey, type dat letter below:"
letter_raw = raw_input("> ")
letter[:0] = letter_raw

for i in letter:
    with open(alph_csv) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            keep = row[i]
            number.append(keep)
            county = len(number)
            count.append(county-1)

count.reverse()
my_dic = dict(zip(count, number))

for key, position in my_dic.items():
    answer = ((26 ** int(key)) * int(position))
    addit.append(answer)

the_answer = sum(addit)
print "your very own number is: "
print the_answer
