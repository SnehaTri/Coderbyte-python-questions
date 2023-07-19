def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def PrimeMover(num):
    count = 0
    candidate = 2
    while count < num:
        if is_prime(candidate):
            count += 1
        candidate += 1
    return candidate - 1

# Example usage
print(PrimeMover(int(input()))) 
