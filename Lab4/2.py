import re

# ---------- Tokenizer ----------
# Matches:
#  - Nonterminal: single uppercase letter optionally followed by a single apostrophe (E or E')
#  - Epsilon: ε
#  - Multi-letter terminal: sequences of lowercase letters (id, num)
#  - Single-char terminal/symbol: + * ( ) etc., or single lowercase letters like i, a, b
token_re = re.compile(r"[A-Z]'?|ε|[a-z]+|[()+*\/\-]|\+")

def tokenize(s):
    s = s.replace(" ", "")
    return token_re.findall(s)

def is_nonterminal(sym):
    return re.fullmatch(r"[A-Z]'?", sym) is not None

# ---------- Input ----------
n = int(input("No. of productions: "))
productions = {}
print("Enter productions (e.g. E->TE'|a):")
for _ in range(n):
    line = input().strip()
    if not line:
        continue
    lhs, rhs = line.split("->")
    parts = rhs.split("|")
    productions[lhs.strip()] = [tokenize(p) for p in parts]

nonterminals = list(productions.keys())

# ---------- FIRST ----------
FIRST = {nt: set() for nt in nonterminals}

def first_of_sequence(seq):
    """Compute FIRST for a sequence of symbols (list). Returns a set that may include 'ε'."""
    res = set()
    for sym in seq:
        if not is_nonterminal(sym):
            res.add(sym)
            return res
        fs = compute_first(sym)
        res |= (fs - {'ε'})
        if 'ε' not in fs:
            return res
    # all symbols can produce ε
    res.add('ε')
    return res

def compute_first(X):
    """Compute FIRST(X) for symbol X (nonterminal or terminal). Uses recursion + memo."""
    if not is_nonterminal(X):
        return {X}
    if FIRST[X]:
        return FIRST[X]
    result = set()
    for prod in productions[X]:
        if prod == ['ε'] or prod == ['ε']:  # explicit epsilon production
            result.add('ε')
            continue
        # prod is a list of tokens
        for sym in prod:
            if not is_nonterminal(sym):
                result.add(sym)
                break
            sub = compute_first(sym)
            result |= (sub - {'ε'})
            if 'ε' not in sub:
                break
        else:
            result.add('ε')
    FIRST[X] = result
    return result

# compute FIRST for all non-terminals
for nt in nonterminals:
    compute_first(nt)

# ---------- FOLLOW (iterative, stable) ----------
FOLLOW = {nt: set() for nt in nonterminals}
FOLLOW[nonterminals[0]].add('$')  # start symbol

changed = True
while changed:
    changed = False
    for A, prods in productions.items():
        for prod in prods:
            # prod is token list
            for i, B in enumerate(prod):
                if not is_nonterminal(B):
                    continue
                beta = prod[i+1:]
                # Add FIRST(beta) - {ε} to FOLLOW(B)
                if beta:
                    f_beta = first_of_sequence(beta)
                    before = len(FOLLOW[B])
                    FOLLOW[B] |= (f_beta - {'ε'})
                    if len(FOLLOW[B]) != before:
                        changed = True
                # If beta is empty or FIRST(beta) contains ε, add FOLLOW(A) to FOLLOW(B)
                if (not beta) or ('ε' in first_of_sequence(beta)):
                    before = len(FOLLOW[B])
                    FOLLOW[B] |= FOLLOW[A]
                    if len(FOLLOW[B]) != before:
                        changed = True

# ---------- Output ----------
def fmt(s):
    return ', '.join(sorted(s))

print("\nFIRST sets:")
for nt in nonterminals:
    print(f"FIRST({nt}) = {{ {fmt(FIRST[nt])} }}")

print("\nFOLLOW sets:")
for nt in nonterminals:
    print(f"FOLLOW({nt}) = {{ {fmt(FOLLOW[nt])} }}")
