def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    :param n: The number to calculate the factorial for.
    :return: The factorial of the number.
    """
    if n < 0:
      raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
      return 1
    else:
      return n * factorial(n - 1)

# Example usage:
if __name__ == "__main__":
    print(factorial(5))
    print(factorial(0))
    print(factorial(1))