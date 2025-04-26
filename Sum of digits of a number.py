# Function to compute the sum of digits of a number
def sum_of_digits(number):
    total = 0  # Initialize sum
    while number > 0:
        digit = number % 10  # Extract the last digit
        total += digit  # Add it to the total
        number = number // 10  # Remove the last digit
    return total

#Example to do sum of digits in a number
num_for_digits_sum = 12345
print("Sum of digits:", sum_of_digits(num_for_digits_sum))
