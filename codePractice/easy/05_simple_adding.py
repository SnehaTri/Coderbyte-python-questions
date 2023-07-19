def SimpleAdding(num):
    if num == 1:
        return 1
    else:
        return num+SimpleAdding(num-1)
    

print(SimpleAdding(int(input())))
