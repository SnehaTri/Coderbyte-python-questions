"""Print all of the numbers from 1 to 100. However, for any number divisible by three, print the word “Fizz,” for any number divisible by five, print the word “Buzz,” 
and for any number divisible by both three and five, print the word “FizzBuzz."""


def fiz_buzz(n):
    for i in range(1, n+1):
        if i%15 == 0:
            print("FizzBuzz", end = " ")
        elif i%3 == 0:
            print("Fizz", end = " ")
        elif i%5 == 0:
            print("Buzz", end =" ")
        else:
            print(i, end=" ")

fiz_buzz(int(input()))
