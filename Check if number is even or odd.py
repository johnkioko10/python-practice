# Function to check if a number is even or odd
def even_or_odd(number):
    if number % 2 == 0: #it means the number will be divided by 2 to check if its even or odd
        return "Even"  # If remainder is 0 when divided by 2 it means it's even
    else:
        return "Odd"   # If not the number is odd

#Example to check if number is even or odd
number = 1937
print(f"{number} is", even_or_odd(number))#One example using odd number

number = 1936
print(f"{number} is", even_or_odd(number))#One example using even number