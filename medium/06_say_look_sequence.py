# Using the Python language, have the function LookSaySequence(num) take the num parameter being passed and return the
# next number in the sequence according to the following rule: to generate the next number in a sequence read off the
# digits of the given number, counting the number of digits in groups of the same digit. For example, the sequence
# beginning with 1 would be: 1, 11, 21, 1211, ... The 11 comes from there being "one 1" before it and the 21 comes
# from there being "two 1's" before it. So your program should return the next number in the sequence given num.


def LookSaySequence(num):
    num_str = str(num)
    count = 1
    result = ""
    
    for i in range(1, len(num_str)):
        if num_str[i] == num_str[i-1]:
            count += 1
        else:
            result += str(count) + num_str[i-1]
            count = 1
    
    result += str(count) + num_str[-1]
    return int(result)

print(LookSaySequence(int(input())))
