"""
Day 9 Project: Credit Card Validator

"""

# Accept card number
# card_number = list(input("Enter your card number:", ).strip())
card_number = list("5893804115457289")

# Apply Luhn algorithm for validating the card number
# 1. Remove the last digit from the card number
check_dgt = card_number.pop()

# 2. Reverse the remaining digits
card_number.reverse()

# Double the even indices and any results are grater than 9 subtract 9
processed_digit = []
for idx, digit in enumerate(card_number):
    number = int(digit)
    if (idx % 2) == 0:
        number *= 2
        if number > 9:
            number -= 9
    processed_digit.append(number)

# Add all the digits and checking digit
total = sum(processed_digit) + int(check_dgt)

# Validation
if total % 10 == 0:
    print("The card is valid!")
else:
    print("The card is invalid!")
