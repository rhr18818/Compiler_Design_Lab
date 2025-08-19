s = input("Enter a string with only 'a' and 'b': ")

if len(s) >= 2 and s[-2:] == "ab":
    print("Valid: String ends with 'ab'")
else:
    print("Invalid: String does not end with 'ab'")


