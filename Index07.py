def get_character(s, n):
    if n < 0 or n >= len(s):
        return False
    return s[n]
print(get_character("uz", 4))   
print(get_character("good", 3)) 
