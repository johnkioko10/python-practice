# Function to reverse a string manually
def reverse_string(s):
    reversed_str = ''  # Start with an empty string
    for char in s:
        reversed_str = char + reversed_str  # Prepend current character
    return reversed_str

#Example using a command for reversing a string
text = "John_Kioko"
print(("Reversed string:", reverse_string(text)))