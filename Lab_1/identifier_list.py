import re

c_keywords = {
    "auto","break","case","char","const","continue","default","do","double",
    "else","enum","extern","float","for","goto","if","inline","int","long",
    "register","restrict","return","short","signed","sizeof","static","struct",
    "switch","typedef","union","unsigned","void","volatile","while"
}
fkdd
fname = input("Enter C file path: ")
text = open(fname).read()
text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
text = re.sub(r'//.*', '', text)
text = re.sub(r'"(?:\\.|[^"\\])*"', '', text)
text = re.sub(r"'(?:\\.|[^'\\])*'", '', text)
idents = set(re.findall(r'\b[_a-zA-Z][_a-zA-Z0-9]*\b', text))
idents -= c_keywords
for name in sorted(idents):
    print(name)
