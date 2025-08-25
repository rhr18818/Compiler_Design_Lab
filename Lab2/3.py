s = input("Enter a string with only 'a' and 'b': ")

i = 0
while i < len(s) and s[i] == 'a':
    i += 1

while i < len(s) and s[i] == 'b':
    i += 1

if i == len(s):
    print("Valid: Matches a^m b^n")
else:
    print("Invalid: Does not match a^m b^n")
