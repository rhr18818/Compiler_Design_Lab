import re

s = input("Enter a string with only 'a'and 'b': ")

#regex pattern
pattern = r"^(a|b)*ab$"

# print(re.fullmatch(pattern,s))
if re.fullmatch(pattern,s):
    print("Valid: String ends with 'ab'")
else:
    print("Invalid: String does not end with 'ab'")