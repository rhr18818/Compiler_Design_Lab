import re

s = input("Enter a string with only 'a'and 'b': ")

#regex pattern
pattern = r"^ab(a|b)*$"

# print(re.fullmatch(pattern,s))
if re.fullmatch(pattern,s):
    print("Valid: String matches ab(a+b)*")
else:
    print("Invalid: String does not match ab(a+b)*")