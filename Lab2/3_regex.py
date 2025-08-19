import re

s = input("Enter a string with only 'a' and 'b': ")

pattern = r"^a*b*$"

if re.fullmatch(pattern, s):
    print("Valid: Matches a^m b^n (all a’s first, then b’s)")
else:
    print("Invalid: Does not match a^m b^n")
