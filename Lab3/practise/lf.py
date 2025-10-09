def LCP(alpha_group):
    prefix = alpha_group[0]
    p_len = len(prefix)
    for s in alpha_group[1:]:
        while prefix != s[0:p_len]:
            p_len-=1
            if p_len == 0:
                return ""
            prefix = prefix[0:p_len]
    return prefix

def left_factoring(grammer):
    updated_grammer={}
    
    for key,prods in grammer.items():
        group={}
        processed_prods = set()
        
        for current_prod in prods:
            if current_prod in processed_prods:
                continue
            alpha_group = [p for p in prods if p.startswith(current_prod[0])]
            alpha = LCP(alpha_group)
            
            if len(alpha_group)>1 and len(alpha)>0:
                print(f"Factoring found in '{key}' with prefix '{alpha}'")

                new_key = key+"'"
                while new_key in grammer or new_key in updated_grammer:
                    new_key+= "'"
                if key not in updated_grammer:
                    updated_grammer[key]=[]
                updated_grammer[key].append(alpha+new_key)
                
                new_rule = []#A'
                for prod in alpha_group:
                    beta = prod[len(alpha):]
                    if not beta:
                        beta = "ε"
                    new_rule.append(beta)
                updated_grammer[new_key]=new_rule
                processed_prods.update(alpha_group)
            else:
                if key not in updated_grammer:
                    updated_grammer[key]=[]
                updated_grammer[key].extend(alpha_group)
                processed_prods.update(alpha_group)
    return updated_grammer

def get_user_grammer():
    new_grammer={}
    print("\n Enter your grammer production(eg,. A->Abc|de) or 'done' to finish")
    while True:
        production_input =input("Production: ").strip()
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
            print("Invalid format. Use 'A->B|C ")
    return new_grammer


grammer = {
    "S": ["iEts","iEtseS","a"]
}
choice = input("Use default grammer for Left Factoring? (yes/no): ").strip().lower()
if choice == "no":
    grammer = get_user_grammer()
    
else:
    print("\nUsing default grammer!")
    
print("Original:", grammer)
print("After removing left recursion:", left_factoring(grammer))
