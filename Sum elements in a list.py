# Function to sum all elements in a list
def sum_of_list(numbers):
    total = 0  # Initialize a variable to store the running total
    for num in numbers:
        total += num  # Add each number to the total
    return total

# Example usage block to test each function
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Sum of list:", sum_of_list(numbers))

