#!/usr/bin/python3

import csv
import sys

file1 = sys.argv[1]

file1_dictionary = {}
with open(file1, newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
     for row in reader:
          word = row[0]
          pinyin = row[1]
          definition = row[2]
          type = row[3]
          file1_dictionary[word] = (word, pinyin, definition, type)

with open(file1, "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t', quotechar='"')
    for row in sorted(file1_dictionary.values()):
        writer.writerow(row)
