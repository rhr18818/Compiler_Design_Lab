import re

fname = input("Enter C file path: ")
text = open(fname).read()
pattern = re.compile(r'//.*|/\*[\s\S]*?\*/')
for m in pattern.finditer(text):
    comment = m.group()
    if comment.startswith("//"):
        print("Single-line:", comment)
    else:
        print("Multi-line:", comment)
