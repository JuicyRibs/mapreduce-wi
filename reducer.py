import sys
import pprint

lines = sys.stdin

occp = {}

for line in lines:
    if(line in occp):
        occp[line]+=1
    else:
        occp[line] = 1


for occu, total in sorted(occp.items()):  # dct.iteritems() in Python 2
        print("{}\t{}".format(occu.replace("\n",""), total))
