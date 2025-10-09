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


def get_user_grammer():
    user_grammer={}
    print("\nEnter your grammer production(eg,. A->Abc|de. 'done' when finished")
    while True:
        production_input = input("Prodcution: ").strip()
        if production_input.lower() == 'done':
            break
        try:
            key,prod_str = production_input.split('->')
            key = key.strip()
            prods = [p.strip() for p in prod_str.split('|')]
            
            if key in user_grammer:
                user_grammer[key].extend(prods)
            else:
                user_grammer[key]=prods
        except ValueError:
            print("Invalid format. Use 'A->B|C' format.")
    return user_grammer
    

grammer = {"A": ["Abc", "Acd", "CD", "XY"]}

choice = input("Use default grammer ? (yes/no) : ").strip().lower()
if choice =='no':
    grammer = get_user_grammer()
else:
    # grammer = default_grammer
    print("\nusing default grammer")

print("Original Grammar:")
for key, prods in grammar.items():
    print(f"{key}->{' | '.join(prods)}")
    
print("\nAfter removing left recursion:")
result = left_recursion(grammar)

for key, prods in result.items():
    print(f"{key}->{' | '.join(prods)}")
