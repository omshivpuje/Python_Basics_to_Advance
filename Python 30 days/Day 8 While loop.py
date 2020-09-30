"""
While loop

Syntax
while condition:
    ... some actions here ...
"""
import random

for number in range(10):
    if number % 2 != 0:
        continue
    print(number)

# Exercise
# 1) Write a short guessing game program using a while loop.
# The user should be prompted to guess a number between 1 and 100,
# and you should tell them whether their guess was too high or too low after each guess.
# The loop should keeping running until the user guesses the number correctly.
user_guess = int(input("Guess and Enter a number between 1 and 100: "))
random_num = random.randint(1, 100)
print('Random number', random_num)

while user_guess != random_num:
    if user_guess > random_num:
        print("Entered guess is too high!")
    else:
        print("Entered guess is too low!")
    user_guess = int(input("Guess and Enter a number between 1 and 100: "))

print("That's a correct guess!", user_guess)

# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
sample_string = "Python"

for character in sample_string:
    if character == "o":
        continue

    print(character)

# 3) Using one of the examples from earlier—or a solution entirely of your own—create a program that
# prints out every prime number between 1 and 100.
primes = []

for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        primes.append(str(dividend))

print(", ".join(primes))
