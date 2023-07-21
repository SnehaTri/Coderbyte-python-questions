#Python program to check if first values are increasing and then decreasing 

def check_list(lst):
    increasing = True
    decreasing = True
    
    # Checking if values are strictly increasing
    for i in range(len(lst)//2):
        if lst[i]+1 != lst[i+1]:
            increasing = False
            break
    
    # Checking if values are strictly decreasing
    for i in range(len(lst)//2, len(lst)-1):
        if lst[i] != lst[i+1]+1:
            decreasing = False
            break
    
    # Checking if both conditions are satisfied
    if increasing and decreasing:
        return True
    else:
        return False

# Example usage
my_list = [1, 2, 3, 4, 2, 1]
result = check_list(my_list)
print(result)
