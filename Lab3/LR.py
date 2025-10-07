def left_recursion(grammar):
    updated_grammar = {}
    for key, prods in grammar.items():
        recursive = []
        non_recursive = []
        for prod in prods:
            if prod.startswith(key):  # left recursive
                print("left recursion found in", key, "->", prod)
                recursive.append(prod[len(key):])  # α
            else:
                non_recursive.append(prod)  # β

        if recursive:
            new_key = key + "'"
            updated_grammar[key] = [beta + new_key for beta in non_recursive]
            updated_grammar[new_key] = [alpha + new_key for alpha in recursive] + ["ε"]
        else:
            updated_grammar[key] = prods
            print("No left recursion found in", key, "->", prod)
    return updated_grammar


# print("="*50)
# Example grammar
# grammar = {"A": ["Aa", "b"]}
grammar = {"A": ["Abc", "Acd", "CD", "XY"]}
print("Original:", grammar)
print("After removing left recursion:", left_recursion(grammar))
