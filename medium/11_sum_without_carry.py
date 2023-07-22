#Sum digits of equal length numbers without carrying forward

def sum_without_cary(num1, num2):
    s = ''
    for x, y in zip(str(num1), str(num2)):
        sum = (int(x) + int(y))%10
        s += str(sum)

    return int(s)

print(sum_without_cary(359, 354))
