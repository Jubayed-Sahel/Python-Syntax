def add(a, b):
    """Returns the sum of two numbers."""         # Doc String must be just write after defining the function 
    return a + b

print(add.__doc__)  # Output: Returns the sum of two numbers.
print("\n\n\n")




def add(a, b , c):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b + c

print(add(2,2,2))
print(add.__doc__)               