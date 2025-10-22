import re

def tokenize(s):
    return re.findall(r"[A-Z]'?|ε|[a-z]+|[()+*\-/$]|id|\+", s.replace(" ", ""))

def is_nt(x): return re.fullmatch(r"[A-Z]'?", x) is not None

n = int(input("No. of productions: "))
p = {}
for _ in range(n):
    l, r = input().split("->")
    p[l.strip()] = [tokenize(x) for x in r.split("|")]

nts = list(p.keys())
FIRST, FOLLOW = {x: set() for x in nts}, {x: set() for x in nts}
FOLLOW[nts[0]].add('$')

def first_seq(seq):
    s = set()
    for x in seq:
        if not is_nt(x): s.add(x); return s
        f = first(x)
        s |= f - {'ε'}
        if 'ε' not in f: return s
    s.add('ε'); return s

def first(X):
    if not is_nt(X): return {X}
    if FIRST[X]: return FIRST[X]
    r = set()
    for pro in p[X]:
        if pro == ['ε']: r.add('ε'); continue
        for x in pro:
            if not is_nt(x): r.add(x); break
            t = first(x); r |= t - {'ε'}
            if 'ε' not in t: break
        else: r.add('ε')
    FIRST[X] = r; return r

for nt in nts: first(nt)

chg = 1
while chg:
    chg = 0
    for A, prods in p.items():
        for pro in prods:
            for i, B in enumerate(pro):
                if not is_nt(B): continue
                beta = pro[i+1:]
                if beta:
                    f = first_seq(beta)
                    old = len(FOLLOW[B])
                    FOLLOW[B] |= f - {'ε'}
                    if len(FOLLOW[B]) != old: chg = 1
                if not beta or 'ε' in first_seq(beta):
                    old = len(FOLLOW[B])
                    FOLLOW[B] |= FOLLOW[A]
                    if len(FOLLOW[B]) != old: chg = 1

print("\nFIRST sets:")
for x in nts: print(f"FIRST({x}) = {{ {', '.join(sorted(FIRST[x]))} }}")

print("\nFOLLOW sets:")
for x in nts: print(f"FOLLOW({x}) = {{ {', '.join(sorted(FOLLOW[x]))} }}")
