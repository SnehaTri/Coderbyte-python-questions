def LetterChanges(a_string):
    new_str = ""
    for letter in a_string:
        if letter == 'z' or letter == 'Z':
            new_str += 'A'
        elif chr(ord(letter)+1) in ['a', 'e', 'i', 'o', 'u']:
            new_str = new_str + chr(ord(letter)+1).upper()
        else:
            new_str = new_str + chr(ord(letter)+1)
    return new_str


print(LetterChanges(input()))
