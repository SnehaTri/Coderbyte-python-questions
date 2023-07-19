# Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string
# using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating character
# and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would
# return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.


def encoded_string(word):
    count = 1
    new_str = ""

    for i in range(1, len(word)):
        if word[i-1] == word[i]:
            count += 1
        else:
            new_str += str(count)+word[i-1]
            count = 1
        
    new_str += str(count)+word[-1]
    return new_str

print(encoded_string(input()))
