import re

x = input()
emails = re.findall(r'[\w\.-]+@[\w\.-]+', x)
print(emails)
