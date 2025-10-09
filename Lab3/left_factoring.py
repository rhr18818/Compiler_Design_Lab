def find_longest_common_prefix(productions):
    """
    Finds the longest common starting prefix among a list of strings
    without using any external modules.
    """
    if not productions:
        return ""

    # Find the shortest production, as the prefix cannot be longer
    shortest_prod = min(productions, key=len)
    
    for i, char in enumerate(shortest_prod):
        # Check if this character is common to all other productions
        for other_prod in productions:
            if other_prod[i] != char:
                # If a mismatch is found, the prefix is the string up to this point
                return shortest_prod[:i]
    
    # If the loop completes, the shortest production itself is the common prefix
    return shortest_prod

def left_factoring(grammar):
    """
    Performs left factoring on a grammar. The grammar is a dictionary
    mapping non-terminals to a list of their productions.
    """
    updated_grammar = {}
    
    for key, productions in grammar.items():
        # A dictionary to group productions by their common prefixes
        groups = {}
        
        # Sort to make grouping easier, though not strictly necessary
        sorted_prods = sorted(productions)
        
        # This set will keep track of productions we've already factored
        processed_prods = set()

        # Iterate through each production to find its group
        for current_prod in sorted_prods:
            if current_prod in processed_prods:
                continue

            # Find all other productions that share a prefix with the current one
            prefix_group = [p for p in sorted_prods if p.startswith(current_prod[0])]
            
            # Find the longest common prefix for the identified group
            prefix = find_longest_common_prefix(prefix_group)
            
            if len(prefix_group) > 1 and len(prefix) > 0:
                print(f"Factoring found in '{key}' with prefix '{prefix}'")
                
                # Create a new non-terminal name (e.g., S')
                new_key = key + "'"
                while new_key in grammar or new_key in updated_grammar:
                    new_key += "'" # Add more primes if needed to ensure uniqueness

                # Add the factored production: A -> prefix A'
                if key not in updated_grammar:
                    updated_grammar[key] = []
                updated_grammar[key].append(prefix + new_key)

                # Create the new rules for A' -> ...
                new_rules = []
                for prod in prefix_group:
                    suffix = prod[len(prefix):]
                    if not suffix:
                        suffix = "ε"  # Use epsilon for an empty suffix
                    new_rules.append(suffix)
                
                updated_grammar[new_key] = new_rules
                processed_prods.update(prefix_group)
            else:
                # If no factoring was done, just add the productions as they are
                if key not in updated_grammar:
                    updated_grammar[key] = []
                updated_grammar[key].extend(prefix_group)
                processed_prods.update(prefix_group)
    
    # Ensure all original keys are present in the final grammar
    for key in grammar:
        if key not in updated_grammar:
            updated_grammar[key] = grammar[key]
            
    return updated_grammar


def get_user_grammar():
    """Gets a grammar from user input."""
    user_grammar = {}
    print("\nEnter grammar productions (e.g., A->abc|ade). Type 'done' when finished.")
    while True:
        production_input = input("Production: ").strip()
        if production_input.lower() == 'done':
            break
        try:
            key, prod_str = production_input.split('->')
            key = key.strip()
            prods = [p.strip() for p in prod_str.split('|')]
            
            if key in user_grammar:
                user_grammar[key].extend(prods)
            else:
                user_grammar[key] = prods
        except ValueError:
            print("Invalid format. Please use 'A -> B | C' format.")
    return user_grammar
    

# --- Main Execution ---

# Default grammar for demonstration
default_grammar = {
    "S": ["iEtS", "iEtSeS", "a"],
    "A": ["abC", "abD", "ef"]
}

choice = input("Use default grammar for Left Factoring? (yes/no): ").strip().lower()
if choice == 'no':
    grammar = get_user_grammar()
else:
    grammar = default_grammar
    print("\nUsing default grammar:")
    
print("Original Grammar:")
for key, prods in grammar.items():
    print(f"{key}->{' | '.join(prods)}")
    
print("\nAfter removing left recursion:")
result = left_recursion(grammar)

for key, prods in result.items():
    print(f"{key}->{' | '.join(prods)}")

