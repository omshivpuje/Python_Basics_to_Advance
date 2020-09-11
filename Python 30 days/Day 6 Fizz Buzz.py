"""One player starts by saying the number 1. Each player then takes it in turns to say the next number, counting one
at a time. If the number is divisible by 3, instead of saying the number, the player should say, "Fizz". If the
number is divisible by 5, instead of saying the number, the player should say, "Buzz". If the number is divisible by
3 and 5, instead of saying the number, the player should say, "Fizz Buzz". If you make a mistake, you're usually
eliminated from the game, and the game continues until there's only a single player remaining. """
for num in range(1, 101):
    if (num % 3 == 0) & (num % 5 == 0):
        print("Fizz Buzz")
    elif num % 5 == 0:
        print("Buzz")
    elif (num % 3) == 0:
        print("Fizz")
    else:
        print(num)
