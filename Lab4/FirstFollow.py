# FIRST & FOLLOW calculator (short + clean output)

g = {}
for _ in range(int(input("No. of productions: "))):
    h, b = input().split("->")
    g[h.strip()] = [x.strip() for x in b.split('|')]

first, follow = {}, {}

def FIRST(x):
    if x not in first: first[x] = set()
    for r in g.get(x, []):
        for c in r:
            if not c.isupper():
                first[x].add(c); break
            first[x] |= (FIRST(c) - {'ε'})
            if 'ε' not in FIRST(c): break
        else: first[x].add('ε')
    return first[x]

def FOLLOW(x):
    if x not in follow: follow[x] = set()
    if x == list(g.keys())[0]: follow[x].add('$')
    for A, rs in g.items():
        for r in rs:
            if x in r:
                i = r.index(x)
                if i + 1 < len(r):
                    y = r[i+1]
                    if y.isupper():
                        follow[x] |= (FIRST(y) - {'ε'})
                        if 'ε' in FIRST(y): follow[x] |= FOLLOW(A)
                    else: follow[x].add(y)
                elif A != x: follow[x] |= FOLLOW(A)
    return follow[x]

for nt in g: FIRST(nt)
for nt in g: FOLLOW(nt)

print("\nFIRST sets:")
for k in g:
    print(f"FIRST({k}) = {{{', '.join(first[k])}}}")

print("\nFOLLOW sets:")
for k in g:
    print(f"FOLLOW({k}) = {{{', '.join(follow[k])}}}")
