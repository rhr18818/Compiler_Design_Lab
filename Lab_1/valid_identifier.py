c_keywords = [
    "auto", "break", "case", "char", "const", "continue", "default", "do", "double",
    "else", "enum", "extern", "float", "for", "goto", "if", "inline", "int", "long",
    "register", "restrict", "return", "short", "signed", "sizeof", "static", "struct",
    "switch", "typedef", "union", "unsigned", "void", "volatile", "while"
]

def is_letter(ch):
    return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')

def is_digit(ch):
    return '0' <= ch <= '9'

def is_valid_identifier(s):
    if len(s) == 0:
        return False
    if s in c_keywords:
        return False
    if not (is_letter(s[0]) or s[0] == '_'):
        return False
    for ch in s[1:]:
        if not (is_letter(ch) or is_digit(ch) or ch == '_'):
            return False
    return True

identifier = input("Enter a string: ")

if is_valid_identifier(identifier):
    print("It is a valid identifier.")
else:
    print("It is NOT a valid identifier.")
