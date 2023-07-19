"""An array of characters and a string B is given. Write a function to return the string B with all the characters from the array removed."""


def str_not_in_arr(arr, str):
    str = "".join([s for s in str if s not in arr])
    return str

print(str_not_in_arr(['a', 'v', 'd', 'r'], 'podklvgtr'))
