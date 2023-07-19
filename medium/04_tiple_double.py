#  Using the Python language, have the function TripleDouble(num1,num2) take both parameters being passed, and return 1
# if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
# For example: if num1 equals 451999277 and num2 equals 41177722899, then return 1 because in the first parameter you
# have the straight triple 999 and you have a straight double, 99, of the same number in the second parameter.
#  If this isn't the case, return 0.


def TripleDouble(num1, num2):
    num1 = str(num1)
    num2 = str(num2)

    for i in range(len(num1)-2):
        if num1[i] == num1[i+1] == num1[i+2]:
            if num2.count(num1[i]*2) == 1:
                return True
            
    return False

print(TripleDouble(int(input()), int(input())))
