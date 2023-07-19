# Using the Python language, have the function NumberEncoding(str) take the str parameter and encode the message
# according to the following rule: encode every letter into its corresponding numbered position in the alphabet.
# Symbols and spaces will also be used in the input. For example: if str is "af5c a#!" then your program should
# return 1653 1#!.

def NumberEncoding(sen):
    enc_sen = ""
    for w in sen:
        if w.isalpha():
            enc_sen += str(ord(w.lower())-96)
        else:
            enc_sen += w
    return enc_sen


print(NumberEncoding("af5c a#!"))
