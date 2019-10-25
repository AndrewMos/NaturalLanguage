import re

filepath = 'file.csv'
fp = open(filepath, 'r')
for line in fp:
    if (not bool(re.match(r'.*\;( )*[\+\-]?[0-9]*\;( )*[\+\-]?[0-9]*\s', line))):
        print("Error in: "+line)
