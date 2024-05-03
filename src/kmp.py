def build_prefix_table(needle):
   
    prefix_table = [0] * len(needle)
    j = 0
    for i in range(1, len(needle)):
        while j > 0 and needle[i] != needle[j]:
            j = prefix_table[j - 1]
        if needle[i] == needle[j]:
            j += 1
        prefix_table[i] = j
    return prefix_table

def kmp_search(haystack, needle):
   

    prefix_table = build_prefix_table(needle)
    matches = []
    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = prefix_table[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            matches.append(i - len(needle) + 1)
            j = prefix_table[j - 1]  
            
            j = 0  
    return matches

