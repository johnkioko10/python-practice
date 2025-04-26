# Function to compute factorial recursively
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    else:
        return n * factorial_recursive(n - 1)

#Example for computing a factorial recursively
num_for_fact = 5
print(f"Factorial (recursive) of {num_for_fact}:", factorial_recursive(num_for_fact))
