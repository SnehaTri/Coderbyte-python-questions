def FirstReverse(str):
    return str[-1: -(len(str)+1): -1]

print(FirstReverse(input()))
