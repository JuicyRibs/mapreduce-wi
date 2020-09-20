import sys

lines = sys.stdin

# next(lines)

for line in sorted(lines):
    line = line.strip()
    line = line.split(",")

    # print(line)
    if(line[4] == "55"):
        print(line[98])

