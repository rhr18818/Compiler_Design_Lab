def left_recursion(grammer):
    updated_grammer={}
    
    for key,prods in grammer.items():
        alpha =[]
        beta =[]
        # print("Prods",prods)
        for prod in prods:
            # print("prod",prod)
            if prod.startswith(key):
                print("left recursion found in", key, "->", prod)
                alpha.append(prod[len(key):]) 
            else:
                beta.append(prod)
                
        if alpha:
            new_key = key+"'"
            updated_grammer[key] = [b+new_key for b in beta]
            updated_grammer[new_key] = [a+new_key for a in alpha] + ["ε"]
        else:
            updated_grammer[key]=prods
            print("No left recursion found in", key, "->", prod)
                
    
    return updated_grammer

def get_user_grammer():
    new_grammer={}
    print("\nEnter your grammer production(eg,. A->AbTrc|de. 'done' when finished")
    
    while True:
        production_input = input("Production: ").strip()
        if production_input.lower() == 'done':
            break
        try:
            key,prod_str = production_input.split('->')
            key = key.strip()
            prods = [p.strip() for p in prod_str.split('|')]
            
            if key in new_grammer:
                new_grammer[key].extend(prods)
            else:
                new_grammer[key]=prods
        except ValueError:
            print("Invalid format. Use 'A->B|C' format.")
            
    return new_grammer
    
grammer = {
    "A":["Abc","Acd","CD","XY"]
}
choice = input("Use default grammer ? (yes/no) : ").strip().lower()
if choice =='no':
    grammer = get_user_grammer()
else:
    # grammer = default_grammer
    print("\nusing default grammer")

print("Original Grammer: ",grammer)
print("After removing left recursion:", left_recursion(grammer))
