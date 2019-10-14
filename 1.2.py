import re

filepath = 'file.csv'
fp = open(filepath, 'r')
for line in fp:
    if (not bool(re.search(r'.*\; [0-9]\d*\; [0-9]\d*\s', line))):
        print("Error in: "+line)
