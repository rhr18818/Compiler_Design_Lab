from collections import defaultdict


#-----give wrong for ----S->iEtSS'|a
# S'->eS|ε
# E->b outputsss

FIRST = defaultdict(set)
FOLLOW = defaultdict(set)

def first(X):
    if X in FIRST and FIRST[X]: return FIRST[X]
    if X not in cfg:  
        FIRST[X].add(X)
        return FIRST[X]
    for production in cfg[X]:
        if production == ['ε']:
            FIRST[X].add('ε')
        else:
            for sym in production:
                FIRST[X] |= (first(sym) - {'ε'})
                if 'ε' not in first(sym): break
            else:
                FIRST[X].add('ε')
    return FIRST[X]

def follow(A):
    if not FOLLOW[A] and A == start_symbol: FOLLOW[A].add('$')
    for head, prods in cfg.items():
        for production in prods:
            for i, B in enumerate(production):
                if B == A:
                    rest = production[i+1:]
                    if rest:
                        f = set()
                        for sym in rest:
                            f |= first(sym) - {'ε'}
                            if 'ε' not in first(sym): break
                        else: f.add('ε')
                        FOLLOW[A] |= f - {'ε'}
                        if 'ε' in f: FOLLOW[A] |= follow(head)
                    elif head != A:
                        FOLLOW[A] |= follow(head)
    return FOLLOW[A]
if __name__=="__main__":
    
    cfg = defaultdict(list)
    n = int(input("Enter number of productions: "))
    print("Enter productions :")
    for _ in range(n):
        head, prods = input().split("->")
        head = head.strip()
        for p in prods.split("|"):
            cfg[head].append(p.strip().split())
    for nt in cfg: first(nt)
    start_symbol = list(cfg.keys())[0]
    for nt in cfg: follow(nt)

    print("\nFIRST sets:")
    for nt in cfg:
        print(f"FIRST({nt})= {{{', '.join(FIRST[nt])}}}")

    print("\nFOLLOW sets:")
    for nt in cfg:
        symbols = sorted(FOLLOW[nt])      
        if '$' in symbols:
            symbols.remove('$')             
            symbols.append('$')
        print(f"FOLLOW({nt})= {{{', '.join(symbols)}}}")