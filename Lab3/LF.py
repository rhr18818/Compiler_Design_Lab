def LCP(productions):
    prefix = productions[0]
    p_len = len(prefix)
    
    # print("="*50)
    # print(productions)
    for s in productions[1:]:
        while prefix != s[0:p_len]:
            p_len -= 1
            if p_len == 0:
                return ""
            prefix = prefix[0:p_len]

    return prefix
def left_factoring(grammer):
    updated_grammer ={}
    
    for key,productions in grammer.items():
        # print(f"key: '{key}',productions: '{productions}'")
        groups={}
        procesed_prods = set()
        
        for current_prod in productions:
            # print(f"\nCurrent Prod: '{current_prod}'")
            if current_prod in procesed_prods:
                continue
            prefix_group = [p for p in productions if p.startswith(current_prod[0])]
            # print(f"\nPrefix group: '{prefix_group}'")
            
            prefix = LCP(prefix_group)
            # print(f"\nPrefix: '{prefix}'")
            
            if len(prefix_group)>1 and len(prefix)>0:
                print(f"Factoring found in '{key}' with prefix '{prefix}'")
                
                new_key = key + "'" #A'
                while new_key in grammer or new_key in updated_grammer:
                    new_key += "'" # A'' ,A''', so on 
                
                if key not in updated_grammer:
                    updated_grammer[key] = []
                updated_grammer[key].append(prefix+new_key) # A-> alpha A'
                
                new_rule = [] #for A' 
                for prod in prefix_group:
                    # print(f"Prod: '{prod}'")
                    suffix = prod[len(prefix):] # iEtSes == es
                    if not suffix:
                        suffix = "ε"
                    new_rule.append(suffix)
                    
                updated_grammer[new_key]= new_rule
                procesed_prods.update(prefix_group)
                
            else: #no factoring
                if key not in updated_grammer:
                    updated_grammer[key] = []
                updated_grammer[key].extend(prefix_group)
                procesed_prods.update(prefix_group)
            
    for key in grammer:
        if key not in updated_grammer:
            updated_grammer[key] = grammer[key]
    return updated_grammer
    

def get_user_grammer():
    user_grammer ={}
    print("\nEnter your grammer production(eg,. A->Abc|de. 'done' when finished")
    while True:
        production_input = input("Production: ").strip()
        if production_input.lower() == 'done':
            break
        try:
            key,prod_str = production_input.split('->')
            key=key.strip()
            prods = [p.strip() for p in prod_str.split('|')]
            
            if key in user_grammer:
                user_grammer[key].extend(prods)
            else:
                user_grammer[key]=prods
        except ValueError:
            print("Invalid format. Please use 'A -> B | C' format.")
    
    return user_grammer
        
grammer = {
    "S": ["iEtS", "iEtSeS", "a"],
    "A": ["abC", "abD", "ef"]
}

choice = input("Use default grammer for Left Factoring? (yes/no): ").strip().lower()
if choice == "no":
    grammer = get_user_grammer()
    
else:
    print("\nUsing default grammer!")
    
print("\nOriginal Grammar:", grammer)
factored_grammer = left_factoring(grammer)
print("\nAfter removing left factoring:", factored_grammer)