# Have the function PrimeChecker(num) take num and return 1 if any arrangement of num comes out to be a prime number,
# otherwise return 0. For example: if num is 910, the output should be 1 because 910 can be arranged into 109 or 019,
# both of which are primes.


def prim_checker(num):
    def isprimt(n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    
    def permuntations(s):
        if len(s) == 1:
            return [s]
        perm_list = []
        for i, c in enumerate(s):
            for perm in permuntations(s[:i]+s[i+1:]):
                perm_list.append(c + perm)
        return perm_list
    
    num = str(num)
    perms = permuntations(num)
    for p in perms:
        if isprimt(int(p)):
            return True
    return False


print(prim_checker(int(input())))
