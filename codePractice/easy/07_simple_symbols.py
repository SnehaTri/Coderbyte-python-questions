import string

def SimpleSymbols(sen):
    c = []
    if sen[0] in string.ascii_letters or sen[-1] in string.ascii_letters:
        return False
    for i in range(1, len(sen)-1):
        if sen[i] in string.ascii_letters:
            if sen[i-1] == '+' and sen[i+1] == '+':
                c.append(True)
            else:
                c.append(False)
    if all(c):
        return True
    else:
        return False

# Example usage
print(SimpleSymbols(input()))  # Output: True
