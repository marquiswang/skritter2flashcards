#!/usr/bin/python3

import csv
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
outputfile = sys.argv[3]

file1_dictionary = {}
with open(file1, newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
     for row in reader:
          word = row[0]
          pinyin = row[1]
          definition = row[2]
          type = row[3]
          file1_dictionary[word] = (word, pinyin, definition, type)


file2_dictionary = {}
with open(file2, newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
     for row in reader:
          word = row[0]
          if word in file1_dictionary:
              continue
          pinyin = row[1]
          definition = row[2]
          type = row[3]
          file2_dictionary[word] = (word, pinyin, definition, type)

with open(outputfile, "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t', quotechar='"')
    for row in file2_dictionary.values():
        writer.writerow(row)
