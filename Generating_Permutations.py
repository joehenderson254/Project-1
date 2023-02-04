def perm_gen_lex(string):
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return [string]
    else:
        perms = []
        for i, char in enumerate(string):
            # Form a simpler string by removing the current character
            smaller = string[:i] + string[i+1:]
            # Generate all permutations of the simpler string recursively
            smaller_perms = perm_gen_lex(smaller)
            # Add the removed character to the front of each permutation of the simpler string
            for perm in smaller_perms:
                perms.append(char + perm)
        return perms