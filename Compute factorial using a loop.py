# Function to compute factorial using a loop
def factorial_loop(n):
    result = 1  #Factorial starts from 1
    for i in range(1, n + 1):  # Loop from 1 to n
        result *= i  # Multiply result by each number in sequence
    return result

#Examples for computing a factorial using a loop
num_for_fact = 10
print(f"Factorial (loop) of {num_for_fact}:", factorial_loop(num_for_fact))

