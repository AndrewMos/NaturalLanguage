import re

filepath = 'test.txt'
fp = open(filepath, 'r')
for line in fp:
    print(re.sub('[A-Z][a-z]*', '[anonymized]', line))
