#Function to check values in list are first increasing and then decreasing by 1 

def check_list(lst):
    left, right = 0, len(lst)-1

    while left < len(lst)//2 and right > len(lst)//2:
        if lst[left] + 1 == lst[left+1]:
            left += 1
        if lst[right] + 1 == lst[right-1]:
            right -= 1
    if left == right == len(lst)//2:
        return True
    else:
        return False


# Example usage
my_list = [1, 2, 3, 4, 3, 2, 1]
result = check_list(my_list)
print(result)
