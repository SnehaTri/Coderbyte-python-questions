#to find best pair ina list with maximum length and all numbers from 0 to 5 are present

def best_pair(lst):
    max_length = 0

    for i in range(len(lst)-2):
        for j in range(i+2, len(lst)):
            str = lst[i] + lst[j]
            length = len(str)
            if '0' in str and '1' in str and '2' in str and '3' in str and '4' in str and '5' in str:
                if length > max_length:
                    max_length = length
                    max_str = str
    return max_str

print(best_pair(['103244', '01222222', '50111', '12345']))
