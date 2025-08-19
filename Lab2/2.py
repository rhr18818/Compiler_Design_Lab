s = input("Enter a string with only 'a' and 'b': ")

if len(s) >= 2 and s[0:2] == "ab":
    print("Valid: String matches ab(a+b)*'")
else:
    print("Invalid: String does not match ab(a+b)*")


