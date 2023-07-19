# Using the Python language, have the function DashInsertII(str) insert dashes ('-') between each two odd numbers and
# insert asterisks ('*') between each two even numbers in str. For example: if str is 4546793 the output should be
# 454*67-9-3. Don't count zero as an odd or even number.


def dash_star(sen):
    new_sen = ""
    for i in range(1, len(sen)):
        if int(sen[i-1])%2 == 0 and int(sen[i])%2 == 0:
            new_sen += sen[i-1]+'*'
        elif int(sen[i-1])%2 == 1 and int(sen[i])%2 == 1:
            new_sen += sen[i-1] + '-'
        else:
            new_sen += sen[i-1]
    new_sen += sen[-1]
    return new_sen

print(dash_star(input()))
