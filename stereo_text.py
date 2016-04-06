#!/usr/bin/python
import sys
import string
import re

i = 0
list_lines = list()
list_longest = list()
list_longest = [0,0]

for line in sys.stdin:
    line = string.replace(line,'\n','')
    list_lines.extend([line])

    line_stripped = re.sub(r"\/","",list_lines[i])
    if len(line_stripped) > list_longest[0]:
        list_longest[0] = len(line_stripped)
        list_longest[1] = i

    i += 1

#print "longest line is %i characters, at index %i" % (list_longest[0], list_longest[1])

int_padded = list_longest[0] + 7

for item in list_lines:
    item_stripped = re.sub(r"\/","",item)
    item_3d = re.sub(r' ?\/(.*)\/ ?',r'\1  ',item)
    print "%s%s%s" % (item_stripped," " * (int_padded - len(item_stripped)), item_3d)
