import re

name = input()
surname = input()
phone = input()
code = input()
city = input()

if (not bool(re.match(r'(\b[A-Z]([a-z])*\b)', name))):
    print("Name error")

if (not bool(re.match(r'(\b[A-Z]([a-z])*\b)', surname))):
    print("Surname error")

if (not bool(re.match(r'(\+( )*\d{2}( )*\(\d{2}\)( )*\d{3}( )*-( )*\d{2}( )*-( )*\d{2})', phone))):
    print("Phone error")

if (not bool(re.match(r'^(\b[A-Z]\w*\s*)+$', city))):
     print("City error")

if (not bool(re.match(r'\d{2}-\d{3}', code))):
    print("Code error")
