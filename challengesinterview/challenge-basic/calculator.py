def calculator_basic(num1, num2, operator):
  """
  Perform basic arithmetic operations on two numbers.

  Args:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    operator (str): The operator to perform ('+', '-', '*', '/').

  Returns:
    int or float: The result of the operation.

  Raises:
    ValueError: If the operator is not one of '+', '-', '*', '/'.
    ZeroDivisionError: If division by zero is attempted.
  """
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    if num2 == 0:
      raise ZeroDivisionError("division by zero")
    return num1 / num2
  else:
    raise ValueError("Invalid operator. Use one of '+', '-', '*', '/'")

# Example usage:
if __name__ == "__main__": 
  print(calculator_basic(10, 5, '+'))
  print(calculator_basic(10, 5, '-'))
  print(calculator_basic(10, 5, '*'))
  print(calculator_basic(10, 5, '/'))