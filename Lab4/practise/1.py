import re
def tokenize(s):
    return re.findall(r"[A-Z]'?|ε|[a-z]+|[()+*\-/$]|id|\+",s.replace(" ",""))  #\+ is not necessary here

def is_non_terminal(x):
    return re.fullmatch(r"[A-Z]'?",x) is not None # also can use and True 

n = int(input("No. of productions: "))
p = {}
for _ in range(n):
    l,r = input().split("->")
    p[l.strip()] = [tokenize(s) for s in r.split("|")]

non_terminals = list(p.keys())

# FIRST, FOLLOW = {x: set() for x in non_terminals}, {x: set() for x in non_terminals}
FIRST = {}
FOLLOW = {}
for x in non_terminals:
    FIRST[x] = set()
    FOLLOW[x] = set()

FOLLOW[non_terminals[0]].add('$')

# first calculation
def first(X):
    if not is_non_terminal(X):
        return{X}
    if FIRST[X]: 
        return FIRST[X]
    r = set()
    for pro in p[X]:
        if pro == ['ε']:
            r.add('ε')
            continue
        for x in pro:
            if not is_non_terminal(x):
                r.add(x)
                break
            t = first(x)
            r |= t - {'ε'}
            if 'ε' not in t:
                break
        else:
            r.add('ε')
    FIRST[X] = r
    return r
for nt in non_terminals:
    first(nt) # first called

# follow helper
def first_seq(seq):
    s = set()
    for x in seq:
        if not is_non_terminal(x):
            s.add(x)
            return s
        f = first(x)
        s |= f - {'ε'}
        if 'ε' not in f:
            return s
    s.add('ε')
    return s
# follow without function
chg = 1
while chg:
    chg = 0
    for A,prods in p.items():
        for pro in prods:
            for i,B in enumerate(pro):
                if not is_non_terminal(B):
                    continue
                beta = pro[i+1:]
                if beta:
                    f = first_seq(beta)
                    old = len(FOLLOW[B])
                    FOLLOW[B] |= f - {'ε'}
                    if len(FOLLOW[B]) != old: 
                        chg = 1
                if not beta or 'ε' in first_seq(beta):
                    old = len(FOLLOW[B])
                    FOLLOW[B] |= FOLLOW[A]
                    if len(FOLLOW[B]) != old: chg = 1


print("\nFIRST sets:")
for x in non_terminals:
    print(f"FIRST({x}) = {{{','.join(sorted(FIRST[x]))}}}")
    
print("\nFOLLOW sets:")
for x in non_terminals: print(f"FOLLOW({x}) = {{ {', '.join(sorted(FOLLOW[x]))} }}")