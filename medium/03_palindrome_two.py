# Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter
# is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. The parameter
# entered may have punctuation and symbols but they should not affect whether the string is in fact a palindrome.
# For example: "Anne, I vote more cars race Rome-to-Vienna" should return true.


import string
def pal_with_symb(sen):
    sen = sen.lower()
    sen = [w for w in sen if w not in list(string.punctuation) and w != " "]
    if sen == sen[-1: -(len(sen)+1): -1]:
        return True
    else:
        return False


print(pal_with_symb("Anne, I vote more cars race Rome-to-Vienna"))
