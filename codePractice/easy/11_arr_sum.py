"""An array and a number A is given. Determine if any two numbers within the array sum to A."""

def sum_in_arr(arr, sum):
    for x in arr:
        diff = sum-x
        if diff in arr:
            return True
    return False
